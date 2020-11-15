import itertools


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)

    if end is None:
        ap_gen = itertools.takewhile(lambda n: n < 3, ap_gen)

    return ap_gen
