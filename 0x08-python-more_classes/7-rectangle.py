#!/usr/bin/python3
"""class of Rectangles"""


class Rectangle:
    """defines rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instatiates width and height"""
        self.width = width
        self.height = height
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__width * self__height)

    def perimeter(self):
        if(self.__width == 0 or self.__height == 0):
            return 0
        else:
            return(2 * (self.__width + self.__height))

    def __str__(self):
        if(self.__width == 0 or self.__height == 0):
            return ""
        rectangle = []
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if h != self.__height - 1:
                rectangle.append("\n")
        return("".join(rectangle))

    def __repr__(self):
        return "{}({},{}".format(__class__.__name__,
                                 self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
