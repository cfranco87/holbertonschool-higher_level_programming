#!/usr/bin/python3
"""
Importing Rectangle for Square class
"""


from models.rectangle import Rectangle
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
        self.size = size
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

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
        displays ## rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(' ' * self.x + '#' * self.__width)
    
    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return (f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}")
