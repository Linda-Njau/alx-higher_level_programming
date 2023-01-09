#!/usr/bin/python3
"""checks instance"""


def is_same_class(obj, a_class):
    """defines method to identify instance"""
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
