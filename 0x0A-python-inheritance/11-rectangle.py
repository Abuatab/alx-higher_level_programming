#!/usr/bin/python3
"""Defines a Rectangle subclass-Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square. Must be a positive integer.
        """
        self.integer_validator("size", size)  # Validate the size
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
