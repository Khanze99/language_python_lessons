

def rangetest(*argscheck):
    def onDecorator(func):

        if not __debug__:
            return func

        else:
            def onCall(*args):
                for (ix, low, high) in argscheck:
                    if args[ix] < low or args[ix] > high:
                        errmsg = f'Argument {ix} not in {low}..{high}'
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
