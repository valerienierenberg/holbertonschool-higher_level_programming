#!/usr/bin/python3
for i in range(97, 123):  # in range of lowercase letters
    if i != 101 and i != 113:  # if letter is not 'q' or 'e'
        print("{}".format(chr(i)), end="")  # print as character
