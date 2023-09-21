#!/usr/bin/python3
islower = __import__('7-islower').islower


def islower(c):

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
