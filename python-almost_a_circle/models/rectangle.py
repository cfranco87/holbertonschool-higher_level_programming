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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        """
        getter for width
        """
        return self.__width

    def set_width(self, width):
        """
        setter for width
        """
        self.__width = width

    def get_height(self):
        """
        getter for  height
        """
        return self.__height

    def set_height(self, height):
        """
        setter for height
        """
        self.__height = height

    def get_x(self):
        """
        getter for x
        """
        return self.__x

    def set_x(self, x):
        """
        setter for x
        """
        self.__x = x

    def get_y(self):
        """
        getter for y
        """
        return self.__y

    def set_y(self, y):
        """
        setter for y
        """
        self.__y = y
