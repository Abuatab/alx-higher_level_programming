#!/usr/bin/python3
"""A script that defines a base class to manage other classes"""
import json


class Base:
    """Manages all the classes to avoid duplication.
    Attributes:
        __nb_objects (int): Counts instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.
        Args:
            id (int): The is of the new base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string`"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            var = cls(1, 1)
        elif cls.__name__ == "Square":
            var = cls(1)
        var.update(**dictionary)
        return var

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
