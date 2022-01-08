

class tracer:

    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(a=4, b=5, c=6)


eggs(2, 16)
eggs(4, y=4)

