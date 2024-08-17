#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written"""
    with open(filename, "w") as f:
        return f.write(text)
