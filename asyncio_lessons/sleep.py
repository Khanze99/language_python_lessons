from time import time
from collections import deque
from tornado.ioloop import IOLoop


current = deque()


class sleep:
    def __init__(self, timeout):
        self.deadline = time() + timeout

    def __await__(self):
        def switch_to(coro):
            current.append(coro)
            coro.send(time())

        IOLoop.instance().add_timeout(self.deadline, switch_to, current[0])
        current.pop()
        return (yield)


def coroutine_start(run, *args, **kwargs):
    coro = run(*args, **kwargs)
    current.append(coro)
    coro.send(None)


if __name__ == '__main__':
    async def hello(name, timeout):
        while True:
            now = await sleep(timeout)
            print(f'Hello, {name}!\tts: {now}')

    coroutine_start(hello, "Friends", 1.0)
    coroutine_start(hello, "World", 2.5)
    IOLoop.instance().start()