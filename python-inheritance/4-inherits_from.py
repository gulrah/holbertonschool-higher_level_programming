def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class, or False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
