

def typetest(**argscheck):
    def onDecorator(func):
        allargs = func.__code__.co_varnames[:func.__code__.co_argcount]
        def onCall(*args, **kwargs):
            positionals = list(allargs)[:len(args)]
            for (argname, type_) in argscheck.items():
                if argname in kwargs:
                    if not isinstance(kwargs[argname], type_):
                        raise TypeError(f'Not support type for arg: {argname} - {type_}')
                elif argname in positionals:
                    index = positionals.index(argname)
                    if not isinstance(args[index], type_):
                        raise TypeError(f'Not support type for arg: {argname} - {type_}')
                else:
                    ...
            return func(*args, **kwargs)
        return onCall
    return onDecorator


@typetest(a=int, c=float)
def func(a, b, c, d):
    ...


func(1, 2, 3.0, 4)
func('spam', 2, 99, 4)
