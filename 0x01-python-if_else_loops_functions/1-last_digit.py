#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")

if number < 0:
    last = number % -10
else:
    last = number % 10

if last > 5:  # if last digit is greater than 5...
    print(last, end=" ")  # print spaces instead of \n
    print("and is greater than 5")
elif last == 0:
    print(last, end=" ")
    print("and is 0")
else:  # last digit is less than 6 and not 0
    print(last, end=" ")
    print("and is less than 6 and not 0")
