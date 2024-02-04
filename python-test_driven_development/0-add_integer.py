#!/usr/bin/python3

"""
    Function that adds 2 integers
"""

def add_integer(num1, num2=98):
    """
    Returns an integer: the addition of num1 and num2
    """
    if not (isinstance(num1, int) or isinstance(num1, float)):
        raise TypeError("num1 must be an integer")
    if not (isinstance(num2, int) or isinstance(num2, float)):
        raise TypeError("num2 must be an integer")
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2
