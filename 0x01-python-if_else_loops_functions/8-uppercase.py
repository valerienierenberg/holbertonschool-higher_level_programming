#!/usr/bin/python3
def uppercase(str):  # asokdgjal;
    for i in range(len(str)):  # end of range is strlen
        letter = ord(str[i])  # convert char to int to compare w/ ASCII values
    if letter >= 97 and letter <= 122:  # if lowercase
        letter = letter - 32  # convert to uppercase
        print("{}".format(chr(letter)), end="")  # convert back to char, print
    print()
