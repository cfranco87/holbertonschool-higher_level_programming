#!/usr/bin/python3
"""
Defines a function is_kind_of_class()
"""


def inherits_from(obj, a_class):
    """
    0-lookup.py
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
