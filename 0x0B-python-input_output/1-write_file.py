#!/usr/bin/python3


def write_file(filename="", text=""):
    """Writes a string to a text file, returns number of characters"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        lineNum = myFile.write(text)
        return lineNum
