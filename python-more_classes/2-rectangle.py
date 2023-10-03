#!/usr/bin/python3
"""
defining a rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def area(self):
        """
        Returns current square area
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter
        """
        return self.__width * 2 + self.__height * 2

    @property
    def width(self):
        """
        Getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
