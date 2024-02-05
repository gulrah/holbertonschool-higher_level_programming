#!/usr/bin/python3
"""6-square.py - Defines a Square class with position."""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int) or value < 0:
            raise TypeError("size must be an integer") \
            if not isinstance(value, int) \
                else ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value isn't a tuple of 2 ints.
        """
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with position using '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
