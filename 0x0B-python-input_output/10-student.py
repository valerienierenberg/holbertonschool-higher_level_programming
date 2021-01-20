#!/usr/bin/python3
""" This module contains a class Student that defines a student """


class Student():
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ init method:
            Attributes: self
                        first_name - string
                        last_name - string
                        age - int
            Returns: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json method:
        Args:
            self - object to be returned as dict description
            attrs - attributes
        Return:
            the dictionary description with simple data
            structure (list, dictionary, string, integer and boolean)
            for JSON serialization of an object
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

# (close but no)
#       for (key, value) in self.__dict__.items():
#            if key in attrs:
#                return ({key: value})
