from rangetest1 import rangetest

print(__debug__)


@rangetest((1, 0, 120))
def persinfo(name, age):
    print(f'{name} is {age} old')


@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print(f'birthday = {M}/{D}/{Y}')


class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


persinfo('Bob Smith', 45)
# persinfo('Bob Smith', 200)

birthday(5, 31, 1963)
# birthday(5, 32, 1963)

sue = Person('Sue', 'dev', 100000)
sue.giveRaise(.10)
print(sue.pay)
# sue.giveRaise(1.10)
# print(sue.pay)