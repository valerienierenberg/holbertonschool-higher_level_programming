#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from
    BaseGeometry. It contains instantiation with 'width' and
    'height' """


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

#  can also do
#  self.integer_validator("width", width)
#  self.__width = width
#  self.integer_validatory("height", height)
#  self.__height = height
