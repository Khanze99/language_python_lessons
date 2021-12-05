

class Commuter2:
    def __init__(self, val=0):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)


class Commuter3:
    def __init__(self, val=0):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other


class Commuter4(Commuter2):
    __radd__ = Commuter2.__add__


class Commuter5:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        # if isinstance(other, Commuter5):
        #     other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        return Commuter5(self.val + other)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.val}>'

