#!/usr/bin/python3
for i in reversed(range(ord("a"), ord("z") + 1)):  # +1 for range to include z
    if (i % 2) != 0:  # if it's odd
        i = i - 32  # make it capital
    print("{:c}".format(i), end="")  # :c to print as char
