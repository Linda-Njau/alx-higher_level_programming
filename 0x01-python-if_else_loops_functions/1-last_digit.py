#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if a > 5:
    print(f"last digit of {number:d} is {a:d} and is greater than 5")
elif a == 0:
    print(f"last digit of {number:d} is {a:d} and is 0")
else
    print(f"last digit of {number:d} is {a:d} and is less than 6 and not  0")
