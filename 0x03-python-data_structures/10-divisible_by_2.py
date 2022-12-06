#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_list = [None] * (len(my_list))
    for i in range(len(my_list)):
        for j in range(len(boolean_list)):
            if i / 2 == 0:
                boolean_list[j] = True
            else:
                boolean_list[j] = False
        return boolean_list
