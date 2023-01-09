#!/usr/bin/python3
"""class definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines class square"""

    def __init__(self, size):
        """instatiate size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
