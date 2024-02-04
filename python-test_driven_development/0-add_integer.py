#!/usr/bin/python3

"""
    Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
