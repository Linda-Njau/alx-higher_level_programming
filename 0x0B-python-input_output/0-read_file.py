#!/usr/bin/python3
"""funtion definition"""


def read_file(filename=""):
    """reads and prints to stdout"""
    with open(filename, encoding="utf-8") as file_name:
        print("{}".format(file_name.read()), end="")
