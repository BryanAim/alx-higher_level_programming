#!/usr/bin/python3
def is_same_class(obj, a_class):
    """a function that returns if the object
        is exactly an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
