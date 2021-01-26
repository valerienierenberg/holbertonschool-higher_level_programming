#!/usr/bin/python3
"""Unittest for Base class and all its methods
"""
import unittest
import pep8
import json
import sys
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for Base class and all its methods
    """

    def setUp(self):
        """
        check output of functions that depend on print
        """
        pass

    def test_pep8(self):
        """
        Test that pep8 requirements are met
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Error: Fix PEP8")

    def tearDown(self):
        """
        Set nb_objets variable back to 0
        """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """
        Testing that class docstring exists
        """
        self.assertIsNotNone(Base.__doc__)

    def test_documentation(self):
        """
        Test that all methods exist and contain correct documentation
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_base_object_create(self):
        """
        Test creating an object of class Base
        and ensure id attribute works properly
        checks that nb_objects is incrementing
        """
        obj1 = Base()
        test1 = str(obj1)
        self.assertTrue(test1[:50], '<models.base.Base object at ')
        self.assertTrue(obj1.id, 1)

        obj2 = Base(420)
        test2 = str(obj2)
        self.assertTrue(test2[:50], '<models.base.Base object at ')
        self.assertTrue(obj2.id, 420)

        obj3 = Base()
        test3 = str(obj3)
        self.assertTrue(test3[:50], '<models.base.Base object at ')
        self.assertTrue(obj3.id, 2)

    def test_to_json_string(self):
        """
        Test conversion to json string in to_json_string method
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string([])) is str)
        myDict = {'id': 4, 'width': 3, 'height': 4, 'x': 1, 'y': 3}
        myDict2 = {'id': 3, 'width': 6, 'height': 2, 'x': 1, 'y': 9}
        jsonized = Base.to_json_string([myDict, myDict2])
        self.assertTrue(type(jsonized) is str)
        myDict3 = json.loads(jsonized)
        self.assertEqual(myDict3, [myDict, myDict2])

    def test_from_json_string(self):
        """
        Test conversion from json string in from_json_string method
        """
        string = '[{"id": 4, "width": 3, "height": 4, "x": 1, "y": 3}, \
                {"id": 3, "width": 6, "height": 2, "x": 1, "y": 9}]'
        jsonized = Base.from_json_string(string)
        self.assertEqual(len(jsonized), 2)
        self.assertTrue(type(jsonized) is list)

    def test_create_rect(self):
        """
        Test that creation of rectangle object with create() method works
        """
        rect1 = Rectangle(1, 2, 3)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)

    def test_create_square(self):
        """
        Test that creation of square object with create() method works
        """
        sq1 = Square(5, 5, 5, 4)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_file_loads_from_rect(self):
        """
        Test that file loads from rectangle object
        """
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(1, 2)
        listofrects = [rect1, rect2]
        Rectangle.save_to_file(listofrects)
        listofrects2 = Rectangle.load_from_file()
        self.assertNotEqual(listofrects, listofrects2)

    def test_file_loads_from_square(self):
        """
        Test that file loads from square object
        """
        sq1 = Square(2, 2, 3)
        sq2 = Square(2, 2)
        listofsquares = [sq1, sq2]
        Square.save_to_file(listofsquares)
        listofsquares2 = Square.load_from_file()
        self.assertNotEqual(listofsquares, listofsquares2)

if __name__ == '__main__':
    unittest.main()
