#!/usr/bin/python3
"""
    A function that adds two numbers
"""


def add_integer(a, b=98):
    """ Adds two integer and/or float numbers
    floats are typecasted to ints before addition
    Returns:
        The sum of a and b
    Raises:
        TypeError: If a or b aren't integer and/or float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
