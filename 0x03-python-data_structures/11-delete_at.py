#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    del_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(len(del_list)):
            if i == idx:
                del del_list[idx]
                return del_list

