#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    for x in reversed(range(len(my_list))):
        print("{}".format(my_list[x]))
