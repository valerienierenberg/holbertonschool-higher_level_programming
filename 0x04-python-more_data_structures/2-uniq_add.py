#!/usr/bin/python3


def uniq_add(my_list=[]):

    return (sum(set(my_list)))

# *** set cannot contain duplicate values ***

#    newlist = my_list[:]
#    total = 0

#    for x in range(len(newlist) - 1):
#        if (newlist[x] != newlist[x+1]):
#            total = total + newlist[x+1]
#    return total
# (this gives result of 17.... couldn't quite get this version to work)
