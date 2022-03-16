from .concrete_point import Point


class NoSuchShapeException(Exception):
    pass


# Процедурные фигуры
class Square:
    def __init__(self, topLeft: Point, side: float):
        self.topLeft = topLeft
        self.side = side


class Rectangle:
    def __init__(self, topLeft: Point, height: float, width: float):
        self.topLeft = topLeft
        self.height = height
        self.width = width


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


class Geometry:
    PI = 3.141592653589793

    def area(self, shape):
        if isinstance(shape, Square):
            return shape.side * shape.side

        if isinstance(shape, Rectangle):
            return shape.height * shape.width

        if isinstance(shape, Circle):
            return self.PI * shape.radius * shape.radius
        raise NoSuchShapeException('No such object shape for calculating area')
