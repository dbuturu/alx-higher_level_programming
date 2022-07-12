#!/usr/bin/python3
"""Base module"""

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionaries to json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """json to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """dictionary to instance"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        lo = []
        try:
            with open(filename, 'r') as f:
                lo = cls.from_json_string(f.read())
            for i, e in enumerate(lo):
                lo[i] = cls.create(**lo[i])
        except Exception:
            pass
        return lo
