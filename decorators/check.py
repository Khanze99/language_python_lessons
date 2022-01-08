

traceMe = True


def rangetest(**argscheck):
    return verification(argscheck, lambda arg, vals: arg < vals[0] or arg > vals[1])


def typetest(**argscheck):
    return verification(argscheck, lambda arg, type_: not isinstance(arg, type_))


def valuetest(**argscheck):
    return verification(argscheck, lambda arg, tester: not tester(arg))


def verification(argscheck, failIf):
    """
    Проверка типа аргументов и вхождений
    """
    def onDecorator(func):
        expected = func.__code__.co_varnames[:func.__code__.co_argcount]

        def error(argname, criteria):
            raise TypeError(f'{func.__name__} argument {argname} not {criteria}')

        def onCall(*args, **kwargs):
            positionals = expected[:len(args)]

            for argname, criteria in argscheck.items():
                if argname in kwargs:
                    if failIf(kwargs[argname], criteria):
                        error(argname, criteria)
                elif argname in positionals:
                    index = expected.index(argname)
                    if failIf(args[index], criteria):
                        error(argname, criteria)
            return func(*args, **kwargs)
        return onCall
    return onDecorator
