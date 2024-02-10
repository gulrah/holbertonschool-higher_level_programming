#!/usr/bin/python3
"""Rectangle module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Returns string representation of Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns string representation of Square"""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
