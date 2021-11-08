

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)  # Хороший способ: расширение исходной версии


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)

