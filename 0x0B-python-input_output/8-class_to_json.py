#!/usr/bin/python3
"""A script that returns the dictionary description of an object for
JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of an object."""
    return obj.__dict__
