from .geometric_figure import GeometricFigure
from .color import Color

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle: width={}, height={}, color={}, area={}".format(
            self.width, self.height, self.color.color, self.area()
        )

    @classmethod
    def name(cls):
        return "Rectangle"

