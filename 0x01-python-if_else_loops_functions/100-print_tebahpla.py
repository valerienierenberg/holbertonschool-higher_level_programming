#!/usr/bin/python3
for i in reversed(range(ord("a"), ord("z") + 1)):
    if (i % 2) != 0:
        i = i - 32
    print("{:c}".format(i), end="")
