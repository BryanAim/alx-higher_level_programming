#!/usr/bin/python3


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance """
        if isinstance(attrs, list) is not True:
            return self.__dict__
        else:
            store_dict = self.__dict__
            only_name = {}
            for keys, values in store_dict.items():
                for i in attrs:
                    if keys == i:
                        only_name[keys] = values
            return only_name

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
