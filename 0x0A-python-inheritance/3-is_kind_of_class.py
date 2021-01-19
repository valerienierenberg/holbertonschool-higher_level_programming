#!/usr/bin/python3
""" Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False. """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class method:
        Args:
            obj: object to be tested if it is an instance of,
            or if it is an instance of a class that inherited from, the
            specified class
            a_class: class that is obj is being test against to verify True
            or False
        Returns:
            True if the object is an instance of, or if the object
            is an instance of a class that inherited from, the specified class;
            otherwise False
    """
    return isinstance(obj, a_class)

#  same as:
#  if isinstance(obj, a_class):
#        return True
#    else:
#        return False
