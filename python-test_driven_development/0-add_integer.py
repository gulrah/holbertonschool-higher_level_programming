#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer (default is 98).

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
        OverflowError: If the result is too large for an integer.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or floats")

    result = int(a) + int(b)

    # Check for integer overflow
    if result < -(2**31) or result > (2**31 - 1):
        raise OverflowError("Result is too large for an integer")

    return result
