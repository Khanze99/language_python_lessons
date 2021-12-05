

class SquaresN:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


class Squares:

    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return SquaresN()

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2