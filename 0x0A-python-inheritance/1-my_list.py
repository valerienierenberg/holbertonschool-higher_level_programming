#!/usr/bin/python3
""" This module contains a class MyList that inherits from list """


class MyList(list):
    """ class that inherits from list """
    def print_sorted(self):
        """ print_sorted method
            prints the list sorted in ascending order
        Args:
            self: list to print
        Return:
            None
        """
        print(sorted(self))
