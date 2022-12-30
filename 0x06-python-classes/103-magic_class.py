#!/usr/bin/python3
"""magic class"""

import math


class MagicClass:
    """ defines circle"""

    def __init__(self, radius=0):
        """defines radius
    
        Arg:
            radius- radius of type int or float
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number)'
        self.__radius = radius

    def area(self):
        """return area"""
        return (self.__radius ** 2 * math.pi)

    def circumfrence(self):
        """return circumfrence"""
        return (2 * math.pi * self.__radius)
