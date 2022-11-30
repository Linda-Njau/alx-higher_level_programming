#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
    a = (num % 10) * -1
else:
    a = number % 10
if a > 5:
    print(f"last digit of {number:d} is {a:d} and is greater than 5")
elif 6 > a != 0:
    print(f"last digit of {number:d} is {a:d} and is less than 6 and not 0")
else:
    print(f"last digit of {number:d} is {a:d} and is 0")
