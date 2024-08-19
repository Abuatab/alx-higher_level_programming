#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instan
        ce"""

        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasat
                    tr(self, key)}
        return self.__dict__
