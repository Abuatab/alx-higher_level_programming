#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instan
        ce"""

        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items(
            ) if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
