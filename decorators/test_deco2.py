

def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return onCall


if __name__ == '__main__':

    @tracer
    def spam(a, b, c):
        print(a + b + c)


    @tracer
    def eggs(N):
        print(2 ** N)

    spam(1, 2, 3)
    spam(a=4, b=5, c=6)

    eggs(32)


    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)

        @tracer
        def lastName(self):
            return self.name.split()[-1]

    print('methods...')
    bob = Person('Bob Smith', 500000)
    sue = Person('Sue Jones', 1000000)

    print(bob.name, sue.name)
    sue.giveRaise(.25)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())
