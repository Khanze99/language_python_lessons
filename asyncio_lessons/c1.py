import inspect
from collections import deque
import time
import functools
import types


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add(self, callback):
        self.queue.append(callback)

    def run(self):
        while self.queue:
            callback = self.queue.popleft()
            callback()

    def create_task(self, coroutine):
        task = Task(coroutine, self)
        return task


class Task:
    def __init__(self, coroutine, scheduler: Scheduler):
        self.coroutine = coroutine
        self.scheduler = scheduler
        self.stack = []
        self.schedule()

    def step(self):  # callback
        try:
            self.coroutine.send(None)
        except StopIteration:
            pass
        else:
            self.schedule()

    def schedule(self):
        self.scheduler.add(self.step)


@types.coroutine
def sleep(delay=0):
    d = time.time() + delay

    while True:
        yield
        if d <= time.time():
            break


class Sleep:
    def __init__(self, delay=0):
        self.delay = delay

    def __await__(self):
        delay = time.time() + self.delay

        while True:
            yield
            if delay <= time.time():
                break


async def sleep1(delay=0):
    d = time.time() + delay
    while True:
        yield
        if d <= time.time():
            break


async def coroutine():
    result = 0
    for number in range(10):
        result += number
        print('Now yielding')
        await sleep(1)
    return result


async def tick():
    result = await coroutine()
    print(result)


async def tock():
    for _ in range(10):
        print('Tick!')
        await sleep(1)


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.create_task(tick())
    scheduler.create_task(tock())
    scheduler.run()
