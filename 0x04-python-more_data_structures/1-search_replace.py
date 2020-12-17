#!/usr/bin/python3


def search_replace(my_list, search, replace):

    newlist = my_list[:]

    for x in range(len(newlist)):
        if newlist[x] == search:
            newlist[x] = replace
    return newlist
