class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print(f'get {item}:', end=' ')
        return self.data[item]

    def __iter__(self):
        print('iter =>', end=' ')

        for i in self.data:
            yield i
            print('next:', end='')

    def __contains__(self, item):
        print('contains: ', end=' ')
        return item in self.data


if __name__ == '__main__':
    x = Iters([1, 2, 3, 4, 5])
    print(3 in x)

    for i in x:
        print(i, end=' | ')

    print()
    print([i ** 2 for i in x])
    print(list(map(bin, x)))

    i = iter(x)

    while True:
        try:
            print(next(i), end='@')
        except StopIteration:
            break