#!/usr/bin/python3
for n in range(0, 100):  # for numbers 0 to 99
    if (n != 99):  # for numbers 0 to 98 only
        print("{:02d}, ".format(n), end="")  # print total 2 digits each time
    else:
        print("{:02d}".format(n))  # if == 99, print 99 with newline (no comma)
