#!/usr/bin/python3
"""Defines a Square class with size validation."""
class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes a new Square instance."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
