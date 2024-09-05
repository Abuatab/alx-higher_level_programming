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

    def update(self, *args, **kwargs):
        """Update attributes using *args and **kwargs."""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Returns the str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
