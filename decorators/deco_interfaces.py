

class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print('Trace: ' + item)
        return getattr(self.wrapped, item)


if __name__ == '__main__':
    @Tracer
    class Person:
        def __init__(self, name):
            self.name = name


    bob = Person('Bob')  # Tracer(Person)(args)
    print(bob.name)
    sue = Person('Sue')
    print(sue.name)
    print(bob.name)