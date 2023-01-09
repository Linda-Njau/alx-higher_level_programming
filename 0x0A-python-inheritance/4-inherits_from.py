#!/usr/bin/python3
"""function definition"""


def inherits_from(obj, a_class):
    """defines subclasses"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
