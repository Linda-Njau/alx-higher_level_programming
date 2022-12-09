#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp_list = []
    for x in range(len(my_list)):
        temp_list = [replace if x == search else x for x in my_list]
    return temp_list
