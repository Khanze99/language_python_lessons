

def rangetest(**argscheck):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            print(argscheck)
            code = func.__code__
            expected = code.co_varnames
            for check in argscheck.items():
                name, (low, high) = check
                if name in kwargs and (kwargs[name] < low or kwargs[name] > high):
                    raise TypeError(f'Argument: {name} not allowed with value {kwargs[name]}')

                elif name in args:
                    index = expected.index(name)
                    if args[index] < low or args[index] > high:
                        raise TypeError(f'Argument: {name} not allowed with value {args[index]}')
            return func(*args, **kwargs)
        return onCall
    return onDecorator


@rangetest(a=(1, 10), c=(1, 20))
def f(a, b, c):
    print(a + b + c)


f(1, 2, c=44)


