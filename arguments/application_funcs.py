def tracer(func, *args, **kwargs):
    print(f'Call: {func.__name__} with args {args}, {kwargs}')
    return func(*args, **kwargs)


def func(a, b, c=1, d=2):
    return a + b + c + d


print(tracer(func, 1, 2, c=13, d=15))


def minmax1(*args):
    m = n = args[0]
    for arg in args[1:]:
        if arg < m:
            m = arg
        if arg > n:
            n = arg

    return m, n


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg

    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg

    return res
