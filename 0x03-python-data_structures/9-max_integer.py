#!/usr/bin/python3


def max_integer(my_list=[]):

    if not my_list:
        return
    else:
        max = my_list[1]
        for x in my_list:
            if x > max:
                max = x
        return (max)
