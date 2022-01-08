

class Decorator:
    def __init__(self, C):
        self.C = C

    def __call__(self, *args, **kwargs):
        self.wrapped = self.C(*args, **kwargs)
        return self

    def __getattr__(self, item):
        return getattr(self.C, item)


@Decorator
class C: ...


x = C()  # --> Decorator(C) --> Decorator(C)() __call__
y = C()  # перезатирает

print(id(x))
print(id(y))
