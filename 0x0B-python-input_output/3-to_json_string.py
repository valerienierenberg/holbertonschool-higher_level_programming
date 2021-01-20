#!/usr/bin/python3
""" This module contains a function returns the JSON
    representation of an object (string) """


import json


def to_json_string(my_obj):
    """ to_json string function:
        Args: my_obj - object (string)
        Return: JSON representation of my_obj
    """
    return (json.dumps(my_obj))
