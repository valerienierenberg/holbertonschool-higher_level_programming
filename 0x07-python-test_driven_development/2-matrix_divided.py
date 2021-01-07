#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ matrix_divided method
    Args:
        matrix - matrix of ints or floats (otherwise raise TypeError)
        div - integer, number to divide the matrix values by
    Raises:
        TypeError: if a or b is not an int
    Returns:
        a new matrix, with values of 'matrix' divided by int variable 'div'
    """

    matrix2 = []

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError('matrix must be a matrix (list of lists) of \
        integers/floats')

    len1 = len(matrix[0])

    for x, y in enumerate(matrix):
        if type(y) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
            integers/floats')
        if len(y) != len1:
            raise TypeError('Each row of the matrix must have the same size')
        len1 = len(y)
        matrix2.append(y[:])
        for i, value in enumerate(y):
            if type(value) is not int and type(value) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of \
                integers/floats')
            matrix2[x][i] = round(value / div, 2)
    else:
        return (matrix2)
