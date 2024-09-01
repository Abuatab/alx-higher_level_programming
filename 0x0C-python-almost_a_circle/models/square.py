#!/usr/bin/python3
"""Defines a squar class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Call the Rectangle's init method with size for both width
        and height"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
