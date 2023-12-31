#!/usr/bin/python3
"""A class Square that defines a square"""

class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size
