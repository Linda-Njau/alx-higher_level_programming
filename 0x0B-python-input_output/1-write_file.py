#!/usr/bin/python3
"""function definiton"""


def write_file(filename="", text=""):
    """writes into file"""
    with open(filename, mode='w', encoding='UTF8') as file_name:
      return file_name.write(text)
