#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Returns True if the object is from the specified class"""
    return type(obj) == a_class
