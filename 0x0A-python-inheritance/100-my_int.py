#!/usr/bin/python3


class MyInt(int):
    """Reverses == and !="""
    def __init__(self, item):
        self.item = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
