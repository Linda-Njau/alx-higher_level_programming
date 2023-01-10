#!/usr/bin/python3
"""function definition"""


def append_write(filename="", text=""):
    """appending function"""
    with open(filename, mode='a', encoding='UTF8') as file_name:
        return file_name.write(text)
