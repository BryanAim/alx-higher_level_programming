#!/usr/bin/python3


def from_json_string(my_str):
    """returns an object (Python data structure)
        represented by a JSON string"""
    import json

    if my_str is None:
        return None

    return (json.loads(my_str))
