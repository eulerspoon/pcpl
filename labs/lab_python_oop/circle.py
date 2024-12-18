import math
from .geometric_figure import GeometricFigure
from .color import Color

class Circle(GeometricFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Circle: radius={}, color={}, area={}".format(
            self.radius, self.color.color, self.area()
        )

    @classmethod
    def name(cls):
        return "Circle"

