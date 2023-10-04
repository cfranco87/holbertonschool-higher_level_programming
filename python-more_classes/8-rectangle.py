#!/usr/bin/python3
"""
defining a rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.
        """
        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a 'official' string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("{}({}, {})".format("Rectangle", self.__width, self.__height))

    def set_print_symbol(self):
        """
        Returns any symbol
        """
        Rectangle.print_symbol = symbol

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        comparing two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __del__(self):
        """
        deletes rectangle
        """
        print("{}".format("Bye rectangle..."))

        Rectangle.number_of_instances -= 1
