#!/usr/bin/python3
"""
my list
"""


class MyList(list):
    """
    A custom list class that inherits from built in class
    """


    def print_sorted(self):
        """
        prints sorted list of integers
        """
        print(sorted(self))
