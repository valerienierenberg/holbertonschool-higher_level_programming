#!/usr/bin/python3
""" This module contains a function returns an object
    (Python data structure) represented by a JSON
    string """


import json


def from_json_string(my_str):
    """ to_json string function:
        Args: my_str - JSON string
        Return: object represented by a JSON string
    """
    return (json.loads(my_str))
