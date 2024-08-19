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
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items(
            ) if key in attrs}
        return self.__dict__
