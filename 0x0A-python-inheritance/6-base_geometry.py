#!/usr/bin/python3
""" Creates an empty class called BaseGeometry
"""


class BaseGeometry:
    def __init__(self):
        pass

    def area(self):
        """raise an exception
        """
        raise Exception("area() is not implemented")
