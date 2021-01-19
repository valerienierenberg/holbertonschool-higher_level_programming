README.md for project 0x0A-python-inheritance

0-lookup.py - function that returns the list of available attributes and methods of an object\
1-my_list.py - class MyList that inherits from list: Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)\
2-is_same_class.py - function that returns True if the object is exactly an instance of the specified class ; otherwise False.\
3-is_kind_of_class.py - function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.\
4-inherits_from.py - function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.\
5-base_geometry.py - an empty class BaseGeometry.\
6-base_geometry.py - class BaseGeometry (based on 5-base_geometry.py) with the public instance method: def area(self): that raises an Exception with the message area() is not implemented\
7-base_geometry.py - class BaseGeometry (based on 6-base_geometry.py) with the public instance method: def area(self): that raises an Exception with the message area() is not implemented, as well as a Public instance method: def integer_validator(self, name, value): that validates value.\
8-rectangle.py - class BaseGeometry (based on 7-base_geometry.py) that incorporates instantiation with width and height: def __init__(self, width, height)\
9-rectangle.py - class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)\
10-square.py - class Square that inherits from Rectangle (9-rectangle.py). area() method is implemented.\
11-square.py - class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py). print() prints, and str() returns, the square description: [Square] <width> divided by <height>\
100-my_int.py - class MyInt that inherits from int, but with the == and != operators inverted.\
101-add_attribute.py - function that adds a new attribute to an object if it’s possible. TypeError exception is raised with the message “can’t add new attribute” if the object can’t have a new attribute.
