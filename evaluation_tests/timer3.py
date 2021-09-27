import time

timer = time.time


def total(func, *args, _reps=1000, **kwargs):
    start = timer()
    for i in range(_reps):
        ret = func(*args, **kwargs)

    elapsed = timer() - start

    return elapsed, ret


def bestof(func, *args, _reps=5, **kwargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start

        if elapsed < best: best = elapsed

    return best, ret


def bestoftotal(func, *args, _reps1=5, **kwargs):
    return min(total(func, *args, **kwargs) for i in range(_reps1))

