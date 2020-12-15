#!/usr/bin/python3


def max_integer(my_list=[]):

    for x in my_list:
        if my_list is None:
            return (None)
        else:
            max = my_list[1]
            if x > max:
                max = x
            return (max)
