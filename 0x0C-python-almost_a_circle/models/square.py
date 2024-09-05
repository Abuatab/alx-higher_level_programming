#!/usr/bin/python3
"""Defines a squar class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Call the Rectangle's init method with size for both width
        and height"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (both width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
