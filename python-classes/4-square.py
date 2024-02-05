#!/usr/bin/python3
"""4-square.py - Defines a Square class with a property for size."""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
