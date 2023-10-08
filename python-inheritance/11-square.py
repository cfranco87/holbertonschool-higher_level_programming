#!/usr/bin/python3
"""
Inheriting Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square
    """
    def __init__(self, size):
        """
        Creates new instances of Square.
        """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """
        Returns current square area
        """
        if self.__size == 0:
            return 0
        else:
            return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return ("{} {}/{}".format("[Square]", self.__size, self.__size))
