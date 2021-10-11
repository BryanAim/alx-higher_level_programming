#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """a function that returns if the object
    is an instance of, or if the object is an instance
    of a class that inherited from
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
