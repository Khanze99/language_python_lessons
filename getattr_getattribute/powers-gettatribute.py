

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, item):
        if item == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif item == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'square':
            object.__setattr__(self, '_square', value)
        else:
            object.__setattr__(self, key, value)


if __name__ == '__main__':
    x = Powers(3, 4)
    print(x.square)
    print(x.cube)

    x.square = 5
    print(x.cube)