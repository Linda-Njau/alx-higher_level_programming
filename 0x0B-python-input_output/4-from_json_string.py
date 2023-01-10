#!/usr/bin/python3
""" json module"""
import json


def from_json_string(my_str):
    """python object to json string"""
    return json.loads(my_str)
