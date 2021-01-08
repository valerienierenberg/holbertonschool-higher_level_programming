#!/usr/bin/python3
""" This module contains a function that prints:
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    """ say_my_name method
    Args:
        first_name, last_name - strings
    Raises:
        TypeError: if first_name and last_name are not both strings
    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
