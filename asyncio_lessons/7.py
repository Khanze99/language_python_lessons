import collections
import sys
import types


class Trampoline:
    """ Manage communications between coroutines """
    running = False

    def __init__(self):
        self.queue = collections.deque()

    def add(self, coroutine):
        """ Request that a coroutine be executed """
        self.schedule(coroutine)

    def run(self):
        result = None
        self.running = True

        try:
            while self.running and self.queue:
                func = self.queue.popleft()
                result = func()
            return result
        finally:
            self.running = False

    def stop(self):
        self.running = False

    def schedule(self, coroutine, stack=(), val=None, *exc):
        def resume():
            value = val

            try:
                if exc:
                    value = coroutine.throw(value, *exc)
                else:
                    value = coroutine.send(value)
            except:
                if stack:
                    self.schedule(stack[0], stack[1], *sys.exc_info())
                else:
                    raise

            if isinstance(value, types.GeneratorType):
                self.schedule(value, (coroutine, stack))

            elif stack:
                self.schedule(stack[0], stack[1], value)

        self.queue.append(resume)
