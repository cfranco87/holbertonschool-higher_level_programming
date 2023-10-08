#!/usr/bin/python3
"""
Reading a file
"""


def write_file(filename="", text=""):
    """
    Define how to write a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        print(f.read(), end="")