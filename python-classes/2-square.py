#!/usr/bin/python3
"""2-square.py - Defines a Square class with size validation."""
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
