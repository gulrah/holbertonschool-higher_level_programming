#!/usr/bin/python3
"""
Check if obj is an instance of a class inherited from the class.
"""


def inherits_from(obj, a_class):
    """ Check for direct or indirect inheritance """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
