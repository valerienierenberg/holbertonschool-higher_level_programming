#!/usr/bin/python3
""" This module contains a function that returns a list of lists
    of integers representing the Pascal's triangle of n """


def append_after(filename="", search_string="", new_string=""):
    """ append_after method
        Args:
            filename - name of file (string)
            search_string - string to search for and create the new line after
            new_string - new string to insert on line following search_string
        Returns: None
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                return(f.write(new_string))
