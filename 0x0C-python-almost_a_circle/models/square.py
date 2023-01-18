#!/usr/bin/python3
"""square class definition"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """definition of square"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiate size, x and y"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class with a new instance"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.__x = args[2]
            self.__y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """prints square class representation"""
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                                              self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """returns dictionary representation of the class attributes"""
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}
