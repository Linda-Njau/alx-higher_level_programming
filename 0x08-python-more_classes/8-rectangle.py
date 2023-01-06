#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class of rectangles"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instatiates width and length"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if(self.__width == 0 or self.__height == 0):
            return 0
        else:
            return(2 * (self.__width + self.__height))

    def __str__(self):
        if(self.__width == 0 or self.___height == 0):
            return ""
        rectangle = []
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle.append(self.print_symbol)
            if h != self.__height - 1:
                rectangle.append("\n")
        return("".join(rectangle))

    def __repr__(self):
        return "{}({}, {}".format(__class__.__name__,
                                  self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1
