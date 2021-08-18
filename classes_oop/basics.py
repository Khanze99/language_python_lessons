

class FirstClass:

    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()


x.set_data("King Arthur")
y.set_data(3.14159)
x.data = "New value"


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


z = SecondClass()
z.set_data(42)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return 'ThirdClass: %s' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
b = a + 'xyz'

a.mul(3)


class rec: pass


rec.name = 'Bob'
rec.age = 40

x = rec()
y = rec()

print(x.name, y.name)
x.name = 'Sue'

print(rec.__dict__.keys())
print(x.__dict__.keys(), y.__dict__.keys())
print(x.__class__)
print(rec.__bases__)


def uppername(obj):
    return obj.name.upper()


print(uppername(x))

rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))