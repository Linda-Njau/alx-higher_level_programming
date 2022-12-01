#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    if arg == 2:
        print("{:d} argument:".format(arg - 1))
    elif arg == 1:
        print("0 arguments.")
    elif arg > 2:
        print("{:d} arguments:".format(arg -1))
    for i in range(1, arg):
        print("{:d} : {:s}".format(i, (argv[i])))
