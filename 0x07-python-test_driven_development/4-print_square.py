#!/usr/bin/python3

def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if size < 0:
        raise ValueError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for i in range(size):
        print(("#" * size))
