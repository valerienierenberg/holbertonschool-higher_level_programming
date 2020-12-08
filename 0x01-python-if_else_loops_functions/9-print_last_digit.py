#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)  # abs value needed for last digit of neg #s
    print((number % 10), end="")  # print last digit with no new line
    return (number % 10)  # return last digit
