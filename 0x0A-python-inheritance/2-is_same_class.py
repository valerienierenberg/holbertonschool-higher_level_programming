#!/usr/bin/python3
""" This module contains a class MyList that inherits from list """


def is_same_class(obj, a_class):
    """ is_same_class method:
        args: obj - object to be tested
              a_class - class that object is being tested against
        return:
            true if object is exactly an instance of a_class
            otherwise false
    """
    return (type(obj) == a_class)
