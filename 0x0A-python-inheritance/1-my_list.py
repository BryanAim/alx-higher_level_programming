#!/usr/bin/python3
""" Creates a class called Mylist
"""


class MyList(list):
    """A class MyList that inherits from list"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """print sorted (ascending sort)"""
        print(sorted(self))
