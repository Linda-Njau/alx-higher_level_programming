#!/usr/bin/python3
"""print square"""


def print_square(size):
    """function to print square sing #
       
    Args:
        size: of type int, l and w of square
    """
    if(isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
