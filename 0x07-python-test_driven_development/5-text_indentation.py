#!/usr/bin/python3
""" This module contains a function that prints a text with 2 new lines after
    each of these characters: ., ?, and : """


def text_indentation(text):
    """ text_indentation method
    Args:
        text: line of text. must be a string
    Raises:
        TypeError: if text is not a string - text must be a string
    Returns:
        None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    c = text.replace('.', '.\n\n')
    c = c.replace(':', ':\n\n')
    c = c.replace('?', '?\n\n')
    c = c.replace('\n ', '\n')
    print(c, end="")

#    else:
#        for c in text:
#            print(c, end="")
#            if c in chars:
#                print()
#                print()
#            if c == ' ':
#                c.replace(' ', '')
#               c.replace(' ', '')
