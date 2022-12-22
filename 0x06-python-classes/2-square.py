#!/usr/bin/python3
"""class for square"""

class Square:
    """class for squares
        Attributes:
            attr1(size): size of square
    """


    def __init__(self, size=0):

        """ initializing size of square
            Args:
                size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
