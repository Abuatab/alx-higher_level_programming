#!/usr/bin/python3
"""A script that defines a base class to manage other classes"""


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
