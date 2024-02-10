#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Returns True if the object from the specified class"""
    return type(obj) is a_class
