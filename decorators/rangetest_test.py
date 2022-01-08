from rangetest import rangetest


@rangetest(age=(0, 120))
def persinfo(name, age):
    print(f'{name} is {age} years old')


@rangetest(M=(1, 12), D=(1, 13), Y=(0, 2013))
def birthday(M, D, Y):
    print(f'birthday = {M}/{D}/{Y}')


# persinfo('Bob', 40)
# persinfo(age=40, name='Bob')

birthday(5, 1, 1963)


# persinfo('Bob', 160)
# birthday(5, D=35, Y=1963)


class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
        self.name = name

    @rangetest(percent=(0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


bob = Person('Bob', 'dev', 1000000)
sue = Person('Sue', 'mgr', 4000000)

bob.giveRaise(.10)
sue.giveRaise(.20)
print(bob.pay, sue.pay)

# bob.giveRaise(1.10)


@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(d=9, c=7, a=1)
# omitargs(d=19, c=17, a=11)
