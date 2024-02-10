#!/usr/bin/python3
"""
Python more Classes
"""


class Rectangle:
    """
    This class represents a rectangle and provides methods to calculate its area and perimeter.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def __ne__(self, other):
        return not self == other

    def __del__(self):
        print("Bye rectangle...")
