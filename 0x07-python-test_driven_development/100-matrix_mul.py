#!/usr/bin/python3
"""Module that contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ matrix_mul method
    Args:
        m_a, m_b: matrices (lists of lists) of integers or floats
    Raises:
        TypeError: if m_a or m_b is not a list
                   if m_a is not a list of lists
                   if one element of the list of lists is not an int or float
                   if m_a or m_b isn't a rectangle (all rows are not same size)
        ValueError: if m_a or m_b is empty
                    if m_a and m_b can't be multiplied
    Returns:
        None
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or type(m_a[0]) is list and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or type(m_b[0]) is list and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
