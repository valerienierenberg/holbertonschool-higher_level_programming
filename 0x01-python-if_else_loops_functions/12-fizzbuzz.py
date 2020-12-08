#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):  # for numbers 1 to 100
        if n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        elif n % 3 and n % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n == 99:  # to get new line at end
            print(n)
        else:
            print(n, end=" ")  # for numbers not divisible by 3 or 5
