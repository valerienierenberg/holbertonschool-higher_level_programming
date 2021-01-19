#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from
    BaseGeometry. It contains instantiation with 'width' and
    'height'. The area method is implemented to return the
    area of the rectangle, and the __str__ magic method is
    prints the proper format """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ init method:
            Attributes: self, width (int), height (int)
            Returns: None
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area method:
            Attributes: self
            Returns: area of rectangle
        """
        return self.__width * self.__height
        # return ("{}".format(self.__width * self.__height))  --- another way

    def __str__(self):
        """ __str__ method:
            Attributes: self
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
