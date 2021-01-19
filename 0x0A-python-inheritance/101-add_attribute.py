#!/usr/bin/python3



class MyClass():
    pass

def add_attribute(obj, name, value):
    """ is_same_class method:
        args: obj - object to create new attribute for
              name - name of attribute
              value - value (string)
        raises: TypeError: if the object can't have new attribute
        return:
            None
    """
    if obj is None or name is None or value is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
