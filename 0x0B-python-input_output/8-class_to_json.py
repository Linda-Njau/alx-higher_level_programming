#!/usr/bin/python3
"""function definition"""
import json


def class_to_json(obj):
    """defines class to json"""
    return json.dumps(obj.__dict__)
