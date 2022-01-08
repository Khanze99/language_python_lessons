

def tracer(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls}, {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(a=4, b=5, c=6)

eggs(2, 10)
eggs(4, y=4)
