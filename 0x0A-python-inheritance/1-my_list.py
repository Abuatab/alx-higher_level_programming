#!/usr/bin/python3
""" A class MyList that inherits from list"""


class MyList(list):
    """A subclass of the list class."""

    def print_sorted(self):
        """Print a sorted list in an an ascending order."""
        print(sorted(self))
