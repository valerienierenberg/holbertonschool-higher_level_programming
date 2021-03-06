#!/usr/bin/python3
""" This module contains a class Square """


class Square:
    """ Square class - represents a square

    Attributes:
        __size : integer, size of a side of the square
    """
    def __init__(self, size):
        """ Initializes a square

        Args:
            size: integer, size of side of square

        Returns: None
        """
        self.__size = size
