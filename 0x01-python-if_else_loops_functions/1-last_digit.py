#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
number = abs(number)  # needed abs value to use mod to get last digit
if (number % 10) > 5:  # if last digit is greater than 5...
    print((number % 10), end=" ")  # print spaces instead of \n
    print("and is greater than 5")
elif (number % 10) == 0:
    print((number % 10), end=" ")
    print("and is 0")
else:  # last digit is less than 6 and not 0
    print((number % 10), end=" ")
    print("and is less than 6 and not 0")
