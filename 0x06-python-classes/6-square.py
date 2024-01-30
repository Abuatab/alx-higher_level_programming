#!/usr/bin/python3
""" A square class """


class Square:
    """ A class for representing a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new square """
        self.size = size
        self.position = position

    def area(self):
        """ computes the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ print the square as a grid of # symbols"""
        if self.__size == 0:
            print()
            return None
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """ returns the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square to the given value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """ returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position to the given value"""
        if not isinstance(value, tuple) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
