#!/usr/bin/python3
""" This module contains a function
    that creates an Object from a “JSON file” """


import json


def load_from_json_file(filename):
    """ load_from_json_file function:
        Args:
            filename - JSON file to create object from
        Return: object created from JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return (json.load(a_file))
