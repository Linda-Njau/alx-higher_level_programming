#!/usr/bin/python3
"""inheritance function"""


class MyList(list):
    """class mylist inherits from list"""

    def print_sorted(self):
        """prints sorted list, ascending"""
        sorted_list = sorted(self)
        print (sorted_list)
