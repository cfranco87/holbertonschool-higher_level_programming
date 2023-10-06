#!/usr/bin/python3
"""
Defines a function is_same_class()
"""


def is_same_class(obj, a_class):
    """
    Return true if the object is an instance we are looking for
    """
    return type(obj) is a_class
