import time

from timerdeco2 import timer


@timer('LC==>')
def listcomp(n):
    return [x*2 for x in range(n)]


@timer('MC==>')
def mapcall(n):
    return list(map(lambda x: x*2, range(n)))


listcomp(10000)
listcomp(100000)
print(listcomp.alltime)

mapcall(10000)
mapcall(100000)
print(mapcall.alltime)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer('GIVE Raise')
    def giveRaise(self, percent):
        self.pay += self.pay * (1.0 + percent)
        time.sleep(1)

    @timer('NAME')
    def firstName(self):
        return self.name.split(' ')[0]


bob = Person('Bob Smith', 100000)
sue = Person('Sue Jones', 400000)

bob.giveRaise(.50)
sue.giveRaise(.50)

print(bob.firstName)
print(sue.firstName)


print(bob.firstName.alltime, sue.firstName.alltime)
print(bob.giveRaise.alltime, sue.giveRaise.alltime)

