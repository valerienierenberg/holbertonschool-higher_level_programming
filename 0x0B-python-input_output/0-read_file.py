#!/usr/bin/python3
""" This module contains a function that reads a
    text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ read_file function:
        Args: filename - string
        Return: None
    """
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            print(a_line, end="")
