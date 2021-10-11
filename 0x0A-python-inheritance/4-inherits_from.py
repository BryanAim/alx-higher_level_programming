#!/usr/bin/python3
def inherits_from(obj, a_class):
    """a function that returns if the object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    if isinstance(obj, a_class) is True and type(obj) is a_class:
        return True
    else:
        return False
