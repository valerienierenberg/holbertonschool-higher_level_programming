#!/usr/bin/python3
""" this modoule contains a function find_peak that finds
a peak in a list of integers """


def find_peak(list_of_integers):
    """finds a peak in a list of integers

    Args:
        list_of_integers (array of ints)
    """
    n = len(list_of_integers)
    # first or last element is peak element
    if (n == 0):
        return
    if (n == 1):
        return list_of_integers[0]
    if (list_of_integers[0] >= list_of_integers[1]):
        return 0
    if (list_of_integers[n - 1] >= list_of_integers[n - 2]):
        return n - 1
    for i in range(1, n - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return i
