#!/usr/bin/python3
"""This module contains a function that multiplies 2 matrices using numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ lazy_ matrix_mul method
    Args:
        m_a, m_b: matrices (lists of lists) of integers or floats
    Returns:
        m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
