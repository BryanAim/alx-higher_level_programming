#!/usr/bin/python3
"""
    A module that divides a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides a matriz"""
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if matrix is None:
        raise TypeError(error1)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(error1)
    if len(matrix[0]) != len(matrix[1]):
            raise TypeError(error2)
    new_list = []
    size = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError(error1)
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(error1)
    return [[round(j / div, 2) for j in i] for i in matrix]
