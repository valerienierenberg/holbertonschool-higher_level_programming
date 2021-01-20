#!/usr/bin/python3
""" Function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False. """


def inherits_from(obj, a_class):
    """ inherits_from method:
        Args:
            obj: object to be tested if it is an instance of a class that
            inherited (directly or indirectly) from the specified class
            a_class: class that is obj is being test against to verify True
            or False
        Returns:
            True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class...
            ... otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
