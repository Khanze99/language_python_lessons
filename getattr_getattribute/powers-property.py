

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    square = property(getSquare, setSquare, doc='square attr')

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube, doc='cube attr')


x = Powers(3, 4)
print(x.square)
print(x.cube)

x.square = 5
print(x.square)