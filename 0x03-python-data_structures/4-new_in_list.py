#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0:
        return copy_list
    if idx >= len(my_list):
        return copy_list
    else:
        for i in range (0, len(copy_list)):
            if i == idx:
                copy_list[idx] = element
                return copy_list
