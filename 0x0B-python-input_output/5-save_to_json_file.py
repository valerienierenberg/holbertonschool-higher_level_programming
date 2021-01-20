#!/usr/bin/python3
""" This module contains a function
    that writes an Object to a text file, using a JSON
    representation """


import json


def save_to_json_file(my_obj, filename):
    """ save_to_json string function:
        Args: my_obj - object to be written to a text file
              filename - text file to be written to
        Return:
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return json.dump(my_obj, a_file)
