#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    my_list2 = my_list.copy()

    for x in range(len(my_list2)):
        if idx < 0 or idx > len(my_list2):
            return (my_list2)
        elif x == idx:
            my_list2[x] = element
            return (my_list2)
