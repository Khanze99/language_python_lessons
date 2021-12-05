# итератор со множественной итерацией


class IterYield:
    def __init__(self, val):
        self.val = val

    def __iter__(self):

        for i in range(self.val):
            yield i
