

def tracer(func):

    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        print(f'call {wrapped.calls} to {func.__name__}')
        return func(*args, **kwargs)
    wrapped.calls = 0
    return wrapped


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
