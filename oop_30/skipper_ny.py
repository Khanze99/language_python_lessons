
class CrNext:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration

        item = self.start
        self.start += 1
        return item


class CrObject:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return CrNext(self.start, self.stop)
