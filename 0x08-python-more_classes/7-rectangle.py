#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """A rectangle representation
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The character to represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.
        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__width) + 2 * (self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if (self.__width == 0) or (self.__height == 0):
            return ""

        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str = rec_str + self.print_symbol
            if i == self.__height - 1:
                break
            rec_str = rec_str + "\n"
        return rec_str

    def __repr__(self):
        """ returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "(Rectangle({}, {}))".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement num of instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
