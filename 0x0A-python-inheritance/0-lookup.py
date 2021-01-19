#!/usr/bin/python3
""" This module contains a function that returns the list of
    available attributes and methods of an object """


def lookup(obj):
    """ lookup method
        Args:
            obj: object to look up to return its attributes and methods
        Return:
            attributes and methods of the obj
        """
    return dir(obj)
