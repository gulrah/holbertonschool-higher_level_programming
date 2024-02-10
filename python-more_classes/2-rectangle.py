#!/usr/bin/python3
"""
More classes
"""


class Rectangle:
    """
    Rectangle class definition with width and height getter/setter methods.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the provided width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
