#!/usr/bin/python3
"""
Reading a file
"""


def read_file(filename=""):
    """
    Define how to read file
    """
    if filename is not None and filename:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
