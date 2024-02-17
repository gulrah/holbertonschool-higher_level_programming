#!/usr/bin/python3
"""Base Module"""

import json

class Base:
    """Base class for other shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
