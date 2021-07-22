

class DiscontNotO:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2

        if self.customer == 'vip':
            return self.price * 0.2


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2


# Extend but don't modify
