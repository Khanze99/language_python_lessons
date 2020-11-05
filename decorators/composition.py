

def d1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


def d2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@d1
@d2
def f():
    print('f')


# эвивалентен следующему:


def f():
    print('f')


f = d1(d2(f))
