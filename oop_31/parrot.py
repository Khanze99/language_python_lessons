

class Action:

    def line(self):
        print(f"{self.name}: {self.say()}")


class Customer(Action):
    name = 'customer'

    def say(self):
        return "something doing"


class Clerk(Action):
    name = 'clerk'

    def say(self):
        return "no, it isn't"


class Parrot(Action):
    name = 'parrot'

    def say(self):
        return None


class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        for instance in (self.customer, self.clerk, self.parrot):
            function = getattr(instance, 'line')
            function()
