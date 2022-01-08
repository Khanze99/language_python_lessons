

def Tracer(aClass):

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapper = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print('Trace: ' + item)
            self.fetches += 1
            return getattr(self.wrapper, item)
    return Wrapper


if __name__ == '__main__':

    @Tracer
    class Spam:
        def display(self):
            print('Spam!' * 8)


    @Tracer
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        def pay(self):
            return self.hours * self.rate


    food = Spam()
    food.display()
    print([food.fetches])

    bob = Person('Bob', 40, 10)
    print(bob.pay())
    print(bob.name)

    print('')
    sue = Person('Sue', 50, 20)
    print(sue.pay())
    print(sue.name)

    print(bob.name)
    print(bob.pay())
    print([bob.fetches, sue.fetches])
