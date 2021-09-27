import time
import sys


timer = time.time


def total(reps, func, *args, **kwargs):
    """
    Total time to run func() reps times
    :param reps:
    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)

    elapsed = timer() - start

    return elapsed, ret


def bestof(reps, func, *args, **kwargs):
    """
    Quickest func() among reps runs
    :param reps:
    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start

        if elapsed < best: best = elapsed

    return best, ret


def bestoftotal(reps1, reps2, func, *args, **kwargs):
    """
    Best of totals
    :param reps1:
    :param reps2:
    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    return bestof(reps1, total, reps2, func, *args, **kwargs)
