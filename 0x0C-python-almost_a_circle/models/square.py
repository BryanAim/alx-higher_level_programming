#!/usr/bin/python3
"""
Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init atribute of class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size propery"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value

    def update(self, *args, **kwargs):
        """updates atributes"""
        new_list = ["id", "size", "x", "y"]
        if args and args != "":
            for i in range(len(args)):
                setattr(self, new_list[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in range(len(new_list)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation"""
        new_dict = {"id": self.id, "size": self.width,
                    "x": self.x, "y": self.y}
        return new_dict
