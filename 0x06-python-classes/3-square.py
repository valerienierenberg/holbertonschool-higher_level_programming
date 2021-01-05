#!/usr/bin/python3
""" This module contains a class Square """


class Square:
    """ Square class - represents a square

    Attributes:
        __size: integer, size of a side of square
    """
    def __init__(self, size=0):
        """ __init method
        Args:
            size: integer
        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ area method
        Args:
            self: square object
        Return:
            the current square area
        """
        return self.__size * self.__size
