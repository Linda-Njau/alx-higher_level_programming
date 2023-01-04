#!/usr/bin/python3
"""prints full name"""


def say_my_name(first_name, last_name=""):
    """print name
        
        Args:
            first_name: type str
            last_name: type str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
