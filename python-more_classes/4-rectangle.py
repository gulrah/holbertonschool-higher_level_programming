#!/usr/bin/python3
"""
More classes
"""


class Rectangle:
    """
    A class representing a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the provided width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.
        """
        return f"Rectangle({self.width}, {self.height})"
