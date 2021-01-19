#!/usr/bin/python3
""" This module contains a class Square that inherits from
    Rectangle. It contains instantiation with 'size' The area method is
    implemented to return the area of the square. str format now
    prints 'Square' instead of 'Rectangle' """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ init method:
            Attributes: self, size (int)
            Returns: None
        """
        super().integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size

    def __str__(self):
        """ __str__ method:
            Attributes: self
        """
        return ("[Sqaure] {}/{}".format(self.__size, self.__size))
