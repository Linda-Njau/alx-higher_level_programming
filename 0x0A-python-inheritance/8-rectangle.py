#!/usr/bin/python3
"""class definiton"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """defines Rectangle subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """instantiate width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height 
