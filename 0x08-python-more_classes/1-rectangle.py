#!/usr/bin/python3
""" This module contains a class Rectangle """


class Rectangle:
    """ Rectangle class - represents a rectangle

    Attributes:
        __height: integer, height of rectangle
        __width: integer, width of rectangle
    """
    def __init__(self, width=0, height=0):
        """ __init method
        Args:
            size: integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for __width
        Returns:
            width of square
        """
        return self.width

    @width.setter
    def width(self, value):
        """ property setter 'width'
        Args:
            value: integer
        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height
        Returns:
            height of square
        """
        return self.height

    @height.setter
    def height(self, value):
        """ property setter 'height'
        Args:
            value: integer
        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
