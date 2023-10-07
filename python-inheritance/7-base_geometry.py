#!/usr/bin/python3
"""
Defining a BaseGeometry
"""


class BaseGeometry:
    """
    Defines a BaseGeometry
    """

    def area(self):
        """
        Returns area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        self.__value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
