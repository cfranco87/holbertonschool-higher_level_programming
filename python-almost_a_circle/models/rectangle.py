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
        Creates new instances of Rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter for width
        """
        self.__width = width

    @property
    def height(self):
        """
        getter for  height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter for height
        """
        self.__height = height

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter for x
        """
        self.__x = x

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for y
        """
        self.__y = y
