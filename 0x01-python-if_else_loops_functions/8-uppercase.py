#!/usr/bin/python3
def uppercase(str):  # asokdgjal;
    for i in range(len(str)):  # alsdkfjalsdfj
        letter = ord(str[i])  # lsadkgjadls
        if letter >= 97 and letter <= 122:  # alsd;kgjals;
            letter = letter - 32  # lasdkfjas;
        print("{}".format(chr(letter)), end="")  # lasdkfjasdkl
    print()
