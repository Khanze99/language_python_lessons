

class User:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def some_behavior(self):
        if type(self.rectangle) is Rectangle:
            self.rectangle.setH(2)
            self.rectangle.setW(5)
        elif type(self.rectangle) is Square:
            self.rectangle.setSide(5)

        return self.rectangle.area()


class Rectangle:
    def __init__(self):
        self.h = 0
        self.w = 0

    def setH(self, h):
        self.h = h

    def setW(self, w):
        self.w = w

    def area(self):
        return self.w * self.h


class Square(Rectangle):
    def setSide(self, side):
        self.h = side
        self.w = side
