def inherits_from(obj, a_class):
    """
    Function to check if obj is an instance of a class
    that inherited (directly or indirectly) from
    the specified class.
    
    Args:
        obj: The object to check.
        a_class: The class to check inheritance against.
        
    Returns:
        True if obj is an instance of a class that
        inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
