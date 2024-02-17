#!/usr/bin/python3
"""Defines a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's position."""
        return self.__x

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's position."""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__validate_non_negative_int('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.__validate_non_negative_int('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position."""
        self.__validate_non_negative_int('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position."""
        self.__validate_non_negative_int('y', value)
        self.__y = value

    def __validate_non_negative_int(self, name, value):
        """Validates if a value is a non-negative integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
