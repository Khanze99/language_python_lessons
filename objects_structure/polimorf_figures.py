from .concrete_point import Point


class Square:
    def __init__(self, topLeft: Point, side: float):
        self.topLeft = topLeft
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, topLeft: Point, height: float, width: float):
        self.topLeft = topLeft
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Circle:
    PI = 3.141592653589793

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius