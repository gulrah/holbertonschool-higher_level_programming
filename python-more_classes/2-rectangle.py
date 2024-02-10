#!/usr/bin/python3
"""
More classes
"""


class Rectangle:
    """
    Represents a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the provided width and height.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.area() == 0:
            return ""
        return '\n'.join(['#' * self._width] * self._height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.
        """
        return f"Rectangle({self._width}, {self._height})"
