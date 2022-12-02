#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv)
    sum = 0
    if number == 1:
        print("0")
    else:
        for i in range(1, number):
            sum += int(sys.argv[i])
        print(sum)
