

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class skipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = skipObject(alpha)

    i = iter(skipper)
    print(next(i), next(i), next(i))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
