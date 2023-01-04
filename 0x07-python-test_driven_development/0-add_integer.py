#!/usr/bin/python3
""" module for adding integers"""


def add_integer(a, b=98):
    """ function adds two integers and returns value"""

    c = 0
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        c = int(a) + int(b)
    return c
