#!/usr/bin/python3
"""class square"""


class Square:
    """class for squares
        Attributes:
            size: size of square
    """
    def __init__(self, size=0):
        """initialize size
            Args:
                size: size of square
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square using #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
