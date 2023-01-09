#!/usr/bin/python3
"""class definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines subclass square of Rectangle"""

    def __init__(self, size):
        """instantiate size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
