#!/usr/bin/python3
"""defines class"""


class Student:
    """defines student"""

    def __init__(self, first_name, last_name, age):
        """instantiates firstname, lastname and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary"""
        if type(attrs) is list:
            for element in attrs:
                if type(element) is str:
                    return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
