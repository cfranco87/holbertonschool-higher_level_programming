#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value), end="")
            print("")
            return True
        else:
            return False
    except ValueError:
            return False

