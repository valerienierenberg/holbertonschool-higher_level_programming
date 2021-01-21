#!/usr/bin/python3
""" This module contains a function that
    adds a new attribute to an object if it’s possible """


def add_attribute(obj, name, value):
    """ is_same_class method:
        args: obj - object to create new attribute for
            name - name of attribute
            value - value (string)
        raises: TypeError: if the object can't have new attribute
        return:
            None
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
