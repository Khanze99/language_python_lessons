import time


timer = time.time


def total(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start

    return elapsed, ret


def bestof(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 5)
    best = 2 ** 32

    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start

        if elapsed < best: best = elapsed

    return best, ret


def bestoftotal(func, *args, **kwargs):
    _reps1 = kwargs.pop('_reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(_reps1))

