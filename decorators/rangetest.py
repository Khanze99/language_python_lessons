

trace = True


def rangetest(**argscheck):
    def onDecorator(func):
        if not __debug__:
            return func

        else:
            code = func.__code__

            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*args, **kwargs):
                expected = list(allargs)
                positionals = expected[:len(args)]
                for (argname, (low, high)) in argscheck.items():
                    if argname in kwargs:
                        if kwargs[argname] < low or kwargs[argname] > high:
                            errmsg = f'{funcname} argument {argname} not in {low}..{high}'
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if args[position] < low or args[position] > high:
                            errmsg = f'{funcname} argument {argname} not in {low}..{high}'
                            raise TypeError(errmsg)
                    else:
                        if trace:
                            print(f'Argument {argname} defaulted')
                return func(*args, **kwargs)
            return onCall
    return onDecorator