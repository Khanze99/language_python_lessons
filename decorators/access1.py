

traceMe = False


def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')


def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get: ', item)
                if item in privates:
                    raise TypeError('private attribute fetch: ' + item)
                else:
                    return getattr(self.wrapped, item)

            def __setattr__(self, key, value):
                trace('set: ', key, value)
                if key == 'wrapped':
                    self.__dict__[key] = value
                elif key in privates:
                    raise TypeError('private attribute change: ' + key)
                else:
                    setattr(self.wrapped, key, value)
        return onInstance
    return onDecorator


if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print(f'{self.label} => {self.data}')

    x = Doubler('X is', [1, 2, 3])
    y = Doubler('Y is', [-10, -20, -30])

    print(x.label)
    x.display(); x.double(); x.display()

    print(y.label)
    y.display(); y.double()
    y.label = 'SPAM'
    y.display()

    print(x.size())
    print(x.data)
    x.data = [1, 1, 1]
    x.size = lambda s: 0
    print(y.data)
    print(y.size())
