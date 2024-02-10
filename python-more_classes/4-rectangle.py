#!/usr/bin/python3
class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """
        Get a string representation of the rectangle for debugging.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __eq__(self, other):
        """
        Check if two rectangles are equal.

        Args:
            other (Rectangle): The other rectangle to compare.

        Returns:
            bool: True if the rectangles are equal, False otherwise.
        """
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def __ne__(self, other):
        """
        Check if two rectangles are not equal.

        Args:
            other (Rectangle): The other rectangle to compare.

        Returns:
            bool: True if the rectangles are not equal, False otherwise.
        """
        return not self == other

    def __del__(self):
        """
        Destructor method to print a message when the rectangle object is deleted.
        """
        print("Bye rectangle...")

# Test cases
my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print(repr(my_rectangle))

# Additional test cases
myrectangle = Rectangle(2, 4)
print(myrectangle)

myrectanglerep = repr(myrectangle)
newrectangle = eval(myrectanglerep)
print(newrectangle)

newrectangle = eval(myrectanglerep)
print(repr(newrectangle))

print(myrectangle != newrectangle)
