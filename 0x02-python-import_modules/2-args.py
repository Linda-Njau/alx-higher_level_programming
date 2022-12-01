#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg == 2:
        print("{:d} argument:".format(arg - 1))
    elif arg == 1:
        print("0 arguments.")
    elif arg > 2:
        print("{:d} arguments:".format(arg -1))
    for i in range(1, arg):
        print("{:d} : {:s}".format(i, (sys.argv[i])))
