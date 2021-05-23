
class Iter:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print('get[%s]:' % index, end='')
        return self.data[index]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('contains:', end='')
        return item in self.data


class YIter:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print('get[%s]:' % index, end='')
        return self.data[index]

    def __iter__(self):
        print('iter=> next: ', end='')
        for x in self.data:
            yield x
            print('next: ', end='')

    def __contains__(self, item):
        print('contains:', end='')
        return item in self.data
