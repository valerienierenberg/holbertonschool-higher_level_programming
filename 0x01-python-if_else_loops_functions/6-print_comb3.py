#!/usr/bin/python3
for a in range(0, 8):  # set first digit range 0-7
    for b in range(a + 1, 10):  # set 2nd digit range 1-9, b is one ahead of a
        print("{:d}{:d}".format(a, b), end=", ")  # print the two digits
print("{:d}{:d}".format(a + 1, b))  # print 89 with newline
