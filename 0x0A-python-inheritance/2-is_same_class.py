#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the class else False"""
    if isinstance(obj, a_class):
        return True
    return False
