#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    if n < 0:
        return (str)
    else:
        string = str[:n] + str[n + 1:]
        return(string)
