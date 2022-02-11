

class Point:
    "Интерфейс координат"
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setCartesian(self, x, y):
        self.x = x
        self.y = y

    def getR(self):
        "Расстояние до начала координат"
        return self.r

    def getTheta(self):
        "Зенитный угол"
        return self.theta

    def setPolar(self, r, theta):
        self.r = r
        self.theta = theta
