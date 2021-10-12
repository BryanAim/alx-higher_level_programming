#!/usr/bin/python3


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)"""
    import json

    if my_obj is None:
        return None

    return (json.dumps(my_obj))
