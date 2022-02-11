from types import FunctionType
from decotools import tracer


class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval, in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = tracer(attrval)
        return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 500000)
sue = Person('Sue Jones', 1000000)

print(bob.name, sue.name)
sue.giveRaise(.10)

print(f'{sue.pay:.2f}')
print(bob.lastName(), sue.lastName())
