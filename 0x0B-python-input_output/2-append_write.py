#!/usr/bin/python3
"""Defines a function that appends to a file"""


def write_file(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns
    the number of characters added"""
    with open(filename, "a") as f:
        return f.write(text)
