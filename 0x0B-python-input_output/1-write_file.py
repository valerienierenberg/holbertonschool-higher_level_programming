#!/usr/bin/python3
""" This module contains a function that writes a string to a
    text file (UTF8) and returns the number of characters written """


def write_file(filename="", text=""):
    """ write_file function:
        Args: filename - string
              text = text to write in the file (string)
        Return: None
    """
    with open(filename, mode='r+', encoding='utf-8') as a_file:
            return(a_file.write(text))
