import sys
import time
import random
from enum import Enum, auto
import heapq
import types


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


@types.coroutine
def sleep(delay):
    yield Op.WAIT, delay


async def launch_rocket(delay, countdown):
    await sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        await sleep(1)
    print("Rocket launched!")


r = launch_rocket(1, 1)


def rockets():
    N = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]


class Op(Enum):
    WAIT = auto()
    STOP = auto()


def now():
    return time.time()


def run_fsm(rockets):
    start = now()
    work = [(start, i, launch_rocket(d, c)) for i, (d, c) in enumerate(rockets)]

    while work:
        step_at, id_, launch = heapq.heappop(work)
        wait = step_at - now()

        if wait > 0:
            time.sleep(wait)

        try:
            op, arg = launch.send(None)
        except StopIteration:
            continue

        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, id_, launch))
        else:
            assert False, op


if __name__ == '__main__':
    run_fsm(rockets())

