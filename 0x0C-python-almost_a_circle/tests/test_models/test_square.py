#!/usr/bin/python3
"""Unittest for Square class and all its methods
"""
import unittest
import pep8
import json
import sys
import os
from io import StringIO
from models import square
from models import rectangle
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class and all its methods
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
        result = pep8style.check_files(['models/square.py'])
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
        self.assertIsNotNone(Square.__doc__)

    def test_documentation(self):
        """
        Test that all methods exist and contain correct documentation
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "create"))
        self.assertTrue(hasattr(Square, "to_json_string"))
        self.assertTrue(hasattr(Square, "from_json_string"))
        self.assertTrue(hasattr(Square, "save_to_file"))
        self.assertTrue(hasattr(Square, "load_from_file"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(Square.create.__doc__)
        self.assertTrue(Square.to_json_string.__doc__)
        self.assertTrue(Square.from_json_string.__doc__)
        self.assertTrue(Square.save_to_file.__doc__)
        self.assertTrue(Square.load_from_file.__doc__)

    def test_square_object_create(self):
        """
        Test creating an object of class Square
        and ensure id attribute works properly
        checks that nb_objects is incrementing
        """
        obj1 = Square(3)
        test1 = str(obj1)
        self.assertTrue(test1[:50], '<models.square.Square object at ')
        self.assertTrue(obj1.id, 1)

        obj2 = Square(3, 1, 1, 420)
        test2 = str(obj2)
        self.assertTrue(test2[:50], '<models.square.Square object at ')
        self.assertTrue(obj2.id, 420)

        obj3 = Square(3)
        test3 = str(obj3)
        self.assertTrue(test3[:50], '<models.square.Square object at ')
        self.assertTrue(obj3.id, 2)

    def test_square_id(self):
        """
        Test that id of square objects is being counted/stored properly
        """
        Base._Base__nb_objects = 0
        r1 = Square(2, 3)
        self.assertEqual(r1.id, 1)
        r2 = Square(3, 33, 5)
        self.assertEqual(r2.id, 2)
        r3 = Square(3, 33, 5, 6)
        self.assertEqual(r3.id, 6)
        r4 = Square(3, 33, 5, 8)
        self.assertEqual(r4.id, 8)
        r5 = Square(3, 33, 5)
        self.assertEqual(r5.id, 3)
        r6 = Square(3, 33, 5, -2)
        self.assertEqual(r6.id, -2)

    def test_argument_number_square(self):
        """
        Test the number of arguments passed to Square class
        ...should raise TypeError if no args passed
        """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_area_args_square(self):
        """
        Test the number of arguments of the method area
        """
        with self.assertRaises(TypeError):
            sq1 = Square()
            self.sq1.area(1)

    def test_square_TypeError_width(self):
        """
        Test for width argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('string')
            Square(None)
            Square(True)
            Square((3, 4))
            Square(float('nan'))
            Square(float('inf'))

    def test_square_TypeError_x(self):
        """
        Test for height argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 'string')
            Square(2, None)
            Square(1, True)
            Square(2, (3, 4))
            Square(2, float('nan'))
            Square(2, float('inf'))

    def test_square_TypeError_y(self):
        """
        Test for x argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, 'string')
            Square(2, 3, None)
            Square(1, 3, True)
            Square(2, 3, (3, 4))
            Square(2, 3, float('nan'))
            Square(2, 3, float('inf'))

    def test_square_ValueError_height(self):
        """
        Test for height ValueError
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4)
            Square(0)
            Square(height=2)

    def test_square_ValueError_x(self):
        """
        Test for x ValueError
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2)
            Square(5, 0)

    def test_square_ValueError_y(self):
        """
        Test for y ValueError
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -2)
            Square(5, 4, 0)

    def test_square_str(self):
        """
        Test that str method for Square class prints correct string format
        """
        Base._Base__nb_objects = 0
        sq1 = Square(2, 4, 2, 9)
        stringrep = str(sq1)
        self.assertEqual(stringrep, "[Square] (9) 4/2 - 2")
        sq2 = Square(2, 4, 2)
        stringrep2 = str(sq2)
        self.assertEqual(stringrep2, "[Square] (1) 4/2 - 2")

    def test_square_to_dictionary(self):
        """
        Test that to_dictionary method for Square class works
        """
        sq1 = Square(2, 1, 1, 7)
        self.assertEqual(sq1.to_dictionary(), {'x': 1, 'y': 1,
                                               'id': 7, 'size': 2})

    def test_square_update(self):
        """
        Test that update method for Square class works
        """
        Base._Base__nb_objects = 0
        sq1 = Square(10, 10, 10)
        sq1.update(size=1)
        stringrep = str(sq1)
        self.assertEqual(stringrep, "[Square] (1) 10/10 - 1")

if __name__ == '__main__':
    unittest.main()
