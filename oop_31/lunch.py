

class Lunch:
    """
    Обед
    """
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(food_name, self.employee)

    @property
    def result(self):
        return self.customer.food


class Customer:
    """
    Покупатель
    """
    def __init__(self):
        self.food = None

    def place_order(self, food_name, employee):
        self.food = employee.take_order(food_name)


class Employee:
    """
    Работник
    """
    def take_order(self, food_name):
        food = Food(food_name)
        return food


class Food:
    """
    Еда
    """
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    lunch = Lunch()
    lunch.order('spagetti')
    print(lunch.result.name)