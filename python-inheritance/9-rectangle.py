#!/usr/bin/python3
"""
Defining a BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle
    """
    def __init__(self, width, height):
        """
        Creates new instances of Rectangle.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
        Returns current square area
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return ("{} {}/{}".format("[Rectangle]", self.__width, self.__height))
