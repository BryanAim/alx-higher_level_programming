#!/usr/bin/python3
"""
    Module to print a square
"""


def print_square(size):
    """ A function that prints a square"""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
