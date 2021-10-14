#!/usr/bin/python3
"""
Base class
"""

import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json strng representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a json representation to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open(filename, "w") as f:
            string = cls.to_json_string(new_list)
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """return list if json representation"""
        new_list = []
        if json_string:
            new_list = json.loads(json_string)
        return new_list

    @classmethod
    def create(cls, **dictionary):
        """Creates a dummy instance and updates it"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """A function that loads from a file and returns a list of instances"""
        filename = cls.__name__ + ".json"
        new_list = []
        try:
            with open(filename, "r") as f:
                lines = f.read()
                lines_converted = cls.from_json_string(lines)
                for i in range(len(lines_converted)):
                    new_list.append(cls.create(**lines_converted[i]))
                return new_list
        except:
            return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            fd = csv.writer(f)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    fd.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    fd.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(filename, 'r') as f:
                fd = csv.reader(f)
                for args in fd:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    new_list.append(obj)
        except:
            pass
        return new_list
