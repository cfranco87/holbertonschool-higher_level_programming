#!/usr/bin/python3
"""
Importing Base for Rectangle class
"""


from .base import Base
"""
import base
"""


class Rectangle(Base):
    """
    Defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call super class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for  height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns current square area
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def display(self):
        """
        0-main.py
        """
        if self.__width == 0 or self.__height == 0:
            return
        for _ in range(self.__height):
            print('#' * self.__width)
