#!/usr/bin/python3
"""Dumps JSON converted objects to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
