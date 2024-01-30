#!/usr/bin/python3
''' A square class '''


class Square:
    ''' A class for representing a square '''
    def __init__(self, size=0):
        ''' Initializes a new square '''
        self.__size = size

        def area(self):
            return self.__size * self.__size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
