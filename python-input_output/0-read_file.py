#!/usr/bin/python3
"""
Reading a file
"""


def read_file(filename=""):
    """
    Define how to read file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
