

class Employee:
    """
    Работник
    """
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        """
        Поднять плату
        :param percent:
        :return:
        """
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        """
        Выполение действия работника, работать
        :return:
        """
        print(self.name, "does stuff")

    def __repr__(self):
        return f"<Employee: name={self.name}, salary={self.salary}>"


class Chef(Employee):
    """
    Работник Шеф-поввар
    """
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        """
        Готовит еду
        :return:
        """
        print(self.name, "makes food")


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        """
        Взаимодействие с клиентом
        :return:
        """
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")


if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.give_raise(0.20)
    print(bob); print()

    for klass in Employee, Chef, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()