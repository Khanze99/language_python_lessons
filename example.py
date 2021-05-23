# 1.iterable - итерирумый, __getitem__, __iter__
# 2. Iterator  __next__


class Items:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        print("call __getitem__")
        return self.items[index]

    def __iter__(self):
        print("call __iter__")
        return iter(self.items)


def myfor(iterable):
    if getattr(iterable, "__iter__", None):
        print("have __iter__")
        iterator = iter(iterable)
        while True:
            try:
                print(next(iterator))
            except StopIteration:
                break
    elif getattr(iterable, "__getitem__", None):
        print("don't have __iter__, but have __getitem__")
        index = 0
        while True:
            try:
                print(iterable[index])
                index += 1
            except IndexError:
                break


class EvenNumIterator:

    def __init__(self, num):
        self.num = num
        self.even_num = [n for n in range(self.num) if n % 2 == 0]
        self._index = 0

    def __iter__(self):
        print("call __iter__")
        return self

    def __next__(self):
        print("call __next__")

        try:
            n = self.even_num[self._index]
            self._index += 1
            return n
        except IndexError:
            raise StopIteration


class EvenNum:
    def __init__(self, num):
        self.num = num
        self.even_num = [n for n in range(self.num) if n % 2 == 0]

    def __iter__(self):
        print("call __iter__")
        return iter(self.even_num)


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self  # потому что метод __next__ является частью самого класса

    def __next__(self):
        if self.stop == self.value:
            raise StopIteration

        self.value += 1
        return self.value ** 2


def gensquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


class YSquares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def gen(self):
        for value in range(self.start, self.stop):
            yield value ** 2
