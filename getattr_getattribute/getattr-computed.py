

class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, item):
        if item == 'x':
            return self.value ** 2
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'x':
            key = 'value'
        self.__dict__[key] = value


if __name__ == '__main__':
    A = AttrSquare(3)
    B = AttrSquare(32)
    print(A.x)
    A.x = 4
    print(A.x)
    print(B.x)
