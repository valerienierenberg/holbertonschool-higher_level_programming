#!/usr/bin/python3


def max_integer(my_list=[]):

    if not my_list:
        return
    else:
        for x in my_list:
            max = my_list[1]
            if x > max:
                max = x
        return (max)
