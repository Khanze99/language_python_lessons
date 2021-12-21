

class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattribute__(self, item):
        if item == 'x':
            return object.__getattribute__(self, 'value') ** 2
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'x':
            key = 'value'
        object.__setattr__(self, key, value)


if __name__ == '__main__':
    A = AttrSquare(3)
    B = AttrSquare(32)
    print(A.x)
    A.x = 4
    print(A.x)
    print(B.x)
