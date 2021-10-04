#!/usr/bin/python3
"""
    Module that indents text
"""


def text_indentation(text):
    """function that indents text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i == ':':
                print("{}\n".format(i))
                flag = 0
            else:
                print("{}".format(i), end="")
