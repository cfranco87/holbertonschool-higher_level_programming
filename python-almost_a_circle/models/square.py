#!/usr/bin/python3
"""
Importing Rectangle for Square class
"""


from .rectangle import Rectangle
"""
import rectangle
"""


class Square(Rectangle):
    """
    Defines a Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call super class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
