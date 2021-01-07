#!/usr/bin/python3
""" This module contains a function that prints a square with #s """


def print_square(size):

    """ print_square method
    Args:
        size - int (length of a side of the square)
    Raises:
        TypeError: if size is not an int, if size is a float and less than 0
        ValueError: if size is less than 0
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print()
