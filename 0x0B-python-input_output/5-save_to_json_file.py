#!/usr/bin/python3
"""json module function"""
import json


def save_to_json_file(my_obj, filename):
    """python text file to json"""
    with open(filename, mode='w') as file_name:
        return json.dump(my_obj, file_name)
