#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                my_list[idx] = element
                return my_list
