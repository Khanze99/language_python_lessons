

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)


def func1(a: 'spam', b, c: 99):
    return a + b + c


print(func1.__annotations__)

for arg in func1.__annotations__:
    print(arg, '=>', func1.__annotations__[arg])


def func2(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func2(1, 2, 3))
print(func2())
print(func2(1, c=10))

print(func2.__annotations__)
