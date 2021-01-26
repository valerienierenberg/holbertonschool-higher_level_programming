#!/usr/bin/python3
""" This module contains a class Base that is the base class
    for all other classes in the 0x0C project """


import json


class Base:
    """ Base class """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """ __init method
        Args:
            self
            id: we can assume id is an integer, and we
                don't need to test the type of it
                - default value of id is set to None
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method
            returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries - a list of dictionaries
        Returns:
            "[]" if list_dictionaries is None or empty
            Otherwise, returns the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is "[]":
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method
            writes the JSON string representation of list_objs to a file
        Args:
            cls - class
            list_objs is a list of instances who inherits of Base -
            example: list of Rectangle or list of Square instances
        Returns:
            string representation of list_objs to a text file
        """
        filename = cls.__name__ + ".json"
        newobj = []
        if list_objs is not None:
            for i in list_objs:
                newobj.append(cls.to_dictionary(i))
                # ^ convert list_objs to dictionary and store it in newobj
        with open(filename, mode='w', encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(newobj))
            # convert newobj dict into json string, and write that to the file

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string method
            returns the list of the JSON string representation json_string
        Args:
            json_string - string representing a list of dictionaries
        Returns:
            list of the JSON string representation json_string
        """
        if json_string is None or json_string is "[]":
            return "[]"
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create method
            returns an instance with all attributes already set
        Args:
            cls - class
            **dictionary - can be thought of as double pointer to a dictionary
            -holds the values of the attributes we are meant to assign
        Returns:
            an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 3)  # have to assign 2 arguments for height & width
        if cls.__name__ is "Square":
            dummy = cls(2)  # only need to assign 1 argument for size
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load_from_file method
            returns a list of instances
        Args:
            cls - class
        Returns:
            If the file doesn’t exist, returns an empty list
            Otherwise, returns a list of instances
        """
        filename = cls.__name__ + ".json"
        newobj = []
        try:
            with open(filename, mode='r', encoding='utf-8') as a_file:
                newobj = cls.from_json_string(a_file.read())
            for i, j in enumerate(newobj):
                newobj[i] = cls.create(**newobj[i])
        except:
            pass
        return (newobj)

#  try to open file to read it (if it doesn't exist, "pass" is enacted...
#  and then our empty list is returned)
#  set the list of the json string representation of the contents of the file..
#  ...equal to newobj
#  iterate through newobj and assign the value at each key to the values
#  read from the file
