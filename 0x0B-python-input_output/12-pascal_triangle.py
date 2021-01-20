#!/usr/bin/python3
""" This module contains a function that returns a list of lists
    of integers representing the Pascal's triangle of n """


def pascal_triangle(n):
    """ pascal_triangle method
        Args:
            n (int)
        Returns: a list of lists of integers representing the
                 Pascal's triangle of n
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
