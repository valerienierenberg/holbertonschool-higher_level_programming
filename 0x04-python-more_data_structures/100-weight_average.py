#!/usr/bin/python3


def weight_average(my_list=[]):

    if not my_list:
        return 0
    a = 0
    b = 0
    for weight in my_list:
        a += (weight[0] * weight[1])
        b += weight[1]
    return (a/b)
