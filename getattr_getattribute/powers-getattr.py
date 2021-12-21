

class Powers:

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, item):
        if item == 'square':
            return self._square ** 2
        elif item == 'cube':
            return self._cube ** 3
        else:
            raise TypeError(f'unknown attr: {item}')

    def __setattr__(self, key, value):
        if key == 'square':
            key = '_square'
        self.__dict__[key] = value


if __name__ == '__main__':
    x = Powers(3, 4)
    print(x.square)
    print(x.cube)
    x.square = 5

    print(x.square)