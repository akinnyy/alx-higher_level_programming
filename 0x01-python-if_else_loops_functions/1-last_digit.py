#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number)% 10
if number > 5:
    print(f"Last digit of {number:d} is {digit:d} and is greater than 5")

elif number == 0:
    print(f"Last digit of {number:d} is {digit:d} and is zero")

elif 0 < number < 6:
    print(f"Last digit of {number:d} is {digit:d} and is less than 6 and not 0")
