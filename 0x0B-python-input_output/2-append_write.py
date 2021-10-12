#!/usr/bin/python3


def append_write(filename="", text=""):
    """Apennds a string to a text file, returns number of characters"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        lineNum = myFile.write(text)
        return lineNum
