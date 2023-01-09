#!/usr/bin/python3
"""class definition"""


class BaseGeometry:
    """defines class"""

    def area(self):
        """defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
