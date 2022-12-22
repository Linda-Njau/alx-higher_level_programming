#!/usr/bin/python3
""" class square"""


class Square:
    """ class of squares
        Attribute:
            size: size of square
    """
    def __init__(self, size=0):
        """ initializing size attribute
            Args:
                size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of square"""
        self.area = self.__size * self.__size
        return self.area
