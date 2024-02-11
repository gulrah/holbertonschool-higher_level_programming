#!/usr/bin/python3
"""Check if obj is an instance of a class inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """Check for direct or indirect inheritance."""
    return isinstance(obj, a_class) and type(obj) is not a_class
