#!/usr/bin/python3
"""define class"""


class Student:
    """defines student"""

    def __init__(self, first_name, last_name, age):
        """instanitates first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict representation of Student instance"""
        return self.__dict__
