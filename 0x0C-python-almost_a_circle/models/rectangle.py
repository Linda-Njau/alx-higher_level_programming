#!/usr/bin/python3
"""class definitions"""
from models.base import Base


class Rectangle(Base):
    """defines Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate width, height, x and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns width * height"""
        return(self.width * self.height)

    def display(self):
        """returns printed rectangle"""
        print(self.y * "\n", end="")
        for h in range(self.height):
            print("{}".format(self.x * " "), end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """prints class representation of a rectangle"""
        return("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id,
                                               self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updates with a new class instance"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns dictionary representation of class"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
