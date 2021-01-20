#!/usr/bin/python3
""" This module contains a function that writes a string to a
    text file (UTF8) and returns the number of characters written """


def append_write(filename="", text=""):
    """ append_write function:
        Args: filename - string
              text = text to write/append to the file (string)
        Return: None
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return(a_file.write(text))
