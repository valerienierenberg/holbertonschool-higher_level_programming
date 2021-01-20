#!/usr/bin/python3
""" This module contains a class Square that inherits from
    Rectangle. It contains instantiation with 'size' The area method is
    implemented to return the area of the square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ init method:
            Attributes: self, size (int)
            Returns: None
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area method:
            Attributes: self
            Returns: area of square
        """
        return self.__size * self.__size
        # return ("{}".format(self.__size * self.__size))  --- another way

    def __str__(self):
        """ __str__ method:
            Attributes: self
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
