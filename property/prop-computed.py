

class PropSquare:
    def __init__(self, start):
        self.value = start

    def getX(self):
        return self.value ** 2

    def setX(self, value):
        self.value = value

    x = property(getX, setX)


P = PropSquare(3)
Q = PropSquare(32)

print(P.x)
P.x = 4

print(P.x)
print(Q.x)