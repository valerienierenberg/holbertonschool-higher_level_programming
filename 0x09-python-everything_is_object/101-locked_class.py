#!/usr/bin/python3
""" This module contains a class LockedClass """


class LockedClass:
    """ Locked class - prevents user from dynamically creating
        new instance attributes, except if the new instance attribute
        is called first_name

    Attributes:
        first_name: string - first name
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """ __init method
        """
        self.first_name = first_name
