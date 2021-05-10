

class Items:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):  # by index
        print('call __getitem__')
        return self.items[index]

    def __iter__(self):  # for, list comp
        print('call __iter__')
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


class EvenNumIterator:  # iterator
    def __init__(self, num: int):
        self.num = num
        self.even_nums = [n for n in range(self.num) if n % 2 == 0]
        self._index = 0

    def __iter__(self):
        print('call __iter__')
        return self

    def __next__(self):
        print('call __next__')
        try:
            n = self.even_nums[self._index]
            self._index += 1
            return n
        except IndexError:
            raise StopIteration


class EvenNum:  # iterate object

    def __init__(self, num: int):
        self.num = num
        self.even_nums = [n for n in range(self.num) if n % 2 == 0]

    def __iter__(self):
        print('call __iter__')
        return iter(self.even_nums)

