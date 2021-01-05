#!/usr/bin/python3
""" This module contains a class Square """


class Square:
    """ Square class """
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
