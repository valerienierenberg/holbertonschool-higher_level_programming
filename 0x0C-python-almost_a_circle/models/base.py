#!/usr/bin/python3
""" This module contains a class Base that is the base class
    for all other classes in the 0x0C project """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init method
        Args:
            self
            id: we can assume id is an integer, and we
                don't need to test the type of it
                - default value of id is set to None
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
