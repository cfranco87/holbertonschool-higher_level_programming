#!/usr/bin/python3
"""
my list
"""


Class MyList:
    """
    Defines a list
    """

    def __init__(self, my_list):
        """
        initializing list
        """
        self.__my_list = my_list


    def print_sorted(self):
        """
        prints sorted list of integers
        """
        sorted_list = sorted(self.__my_list)
        print sorted(sorted_list)
