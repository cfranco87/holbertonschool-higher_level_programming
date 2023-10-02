#!/usr/bin/python3
"""A class Square that defines a square"""

class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data"""
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
