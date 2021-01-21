#!/usr/bin/python3
""" This module contains a class MyInt that inherits from int.
    However, MyInt has == and != operators inverted """


class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """ returns the opposite of equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ returns the opposite of not equal """
        return super().__eq__(other)
