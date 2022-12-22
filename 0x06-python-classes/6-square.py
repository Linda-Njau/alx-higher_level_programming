#!/usr/bin/python3
"""class square"""


class Square:
    """class for squares
        Attributes:
            size: size of square type int
            position: tuple of two +int
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize size and position
            Args:
                size: size of square
                position: position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return     
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square and show position"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__positon[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
