# 0x0C-python-almost_a_circle

## Project Description:

This project is a culmination of everything we have learned about Python thus far, including:

* Import
* Exceptions
* Classes
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
* Serialization/Deserialization
* JSON

Additionally, it incorporates the following newly-introduced topics:

* args and kwargs

All files, classes and methods are unit tested and be PEP 8 validated.

Unittesting can be done with the following command:
`python3 -m unittest discover tests`

## File Organization:

###### models/
* contains the following files:
    - base.py
    - rectangle.py
    - square.py

###### tests/
* contains the following files:
    - test_models/
        - test_base.py
        - test_rectangle.py
        - test_square.py


## File Descriptions:
* base.py - module that contains the class Base with the following methods and attributes:
    - private class attribute __nb_objects, initialized to = 0
    - __init__() - class constructor, with attribute id
    - to_json_string() - returns a json string representation of list_dictionaries
    - save_to_file() - writes the JSON string representation of list_objs to a file
    - from_json_string() - returns list of JSON string representation 'json_string'
    - create() - returns an instance with all attributes already set
    - load_from_file() - returns a list of instances

* rectangle.py - module that contains the class Rectangle with the following methods and attributes:
    - (Rectangle class inherits from class Base)
    - __init__() - class constructor, with attributes self, width, height, x=0, y=0, and id=None
    - public getters and setters for width, height, x, and y
    - area() - returns area of Rectangle object
    - display() - returns printed rectangle with #, taking x and y into account (position on x and y axis)
    - __str__() - returns string representation of Rectangle with format specified in project
    - update() - assigns a key/value argument to attributes: id, width, height, x, y
    - to_dictionary() - returns the dictionary representation of a Rectangle object

* square.py - module that contains the class Square with the following methods and attributes:
    - (Square class inherits from class Rectangle)
    - __init__() - class constructor, with attributes self, size, x=0, y=0, and id=None
    - __str__() - returns string representation of Square with format specified in project
    - public getters and setters for size
    - update() - assigns a key/value argument to attributes: id, size, x, y
    - to_dictionary() - returns the dictionary representation of a Square object

* test_base.py - contains unittest tests for all classes and methods contained in base.py
* test_rectangle.py - contains unittest tests for all classes and methods contained in rectangle.py
* test_square.py - contains unittest tests for all classes and methods contained in square.py
