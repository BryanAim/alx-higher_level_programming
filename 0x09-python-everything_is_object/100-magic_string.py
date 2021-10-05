#!/usr/bin/python3
def magic_string(number=[0]):
    number[0] = number[0] + 1
    return "Holberton, " * (number[0] - 1) + "Holberton, "[:-2]
