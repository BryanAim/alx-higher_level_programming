#!/usr/bin/python3


def pascal_triangle(n):
    """Prints the n-pascal triangle"""
    new_list = []
    if n <= 0:
        new_list = [[]]
        return new_list
    for i in range(0, n):
        new_list.append([1] * (i + 1))
        if i >= 2:
            for j in range(1, len(new_list[i]) - 1):
                new_list[i][j] = new_list[i - 1][j] + new_list[i - 1][j - 1]
    return new_list
