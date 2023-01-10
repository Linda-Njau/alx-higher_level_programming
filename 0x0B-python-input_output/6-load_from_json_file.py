#!/usr/bin/python3
""" json module function"""
import json


def load_from_json_file(filename):
    """creates object"""
    with open(filename, mode='r') as file_name:
        return json.load(file_name)
