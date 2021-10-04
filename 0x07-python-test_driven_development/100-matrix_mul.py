#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len1 = len(m_a)
    temp = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if temp is None:
            temp = len(i)
            if temp == 0:
                raise ValueError("m_a can't be empty")
        if temp != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    len2 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if len2 is None:
            len2 = len(i)
            if len2 == 0:
                raise ValueError("m_b can't be empty")
        if len2 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if temp != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = []
    for i in range(len1):
        l = []
        for j in range(len2):
            num = 0
            for k in range(len1):
                num += m_a[i][k] * m_b[k][j]
            l.append(num)
        new_matrix.append(l)
    return new_matrix
