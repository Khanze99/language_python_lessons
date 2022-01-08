

def rangetest(func):
    def onCall(*args, **kwargs):
        annotations = func.__annotations__
        print(annotations)
        expected = annotations.keys()
        for name, (low, high) in annotations.items():
            if name in kwargs and (kwargs[name] < low or kwargs[name] > high):
                raise TypeError(f'Argument: {name} not allowed with value {kwargs[name]}')

            elif name in args:
                index = expected.index(name)
                if args[index] < low or args[index] > high:
                    raise TypeError(f'Argument: {name} not allowed with value {args[index]}')
        return func(*args, **kwargs)
    return onCall


@rangetest
def spam(a: (1, 10), b: (1, 20)):
    print(a + b)


spam(10, 20)
spam(b=12, a=2)
spam(2, b=12)
spam(12, b=22)