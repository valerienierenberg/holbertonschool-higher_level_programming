#!/usr/bin/python3
"""Unittest for Rectangle class and all its methods
"""
import unittest
import pep8
import json
import sys
import os
from io import StringIO
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class and all its methods
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
        result = pep8style.check_files(['models/rectangle.py'])
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
        self.assertIsNotNone(Rectangle.__doc__)

    def test_documentation(self):
        """
        Test that all methods exist and contain correct documentation
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(hasattr(Rectangle, "create"))
        self.assertTrue(hasattr(Rectangle, "to_json_string"))
        self.assertTrue(hasattr(Rectangle, "from_json_string"))
        self.assertTrue(hasattr(Rectangle, "save_to_file"))
        self.assertTrue(hasattr(Rectangle, "load_from_file"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(Rectangle.create.__doc__)
        self.assertTrue(Rectangle.to_json_string.__doc__)
        self.assertTrue(Rectangle.from_json_string.__doc__)
        self.assertTrue(Rectangle.save_to_file.__doc__)
        self.assertTrue(Rectangle.load_from_file.__doc__)

    def test_rect_object_create(self):
        """
        Test creating an object of class Rectangle
        and ensure id attribute works properly
        checks that nb_objects is incrementing
        """
        obj1 = Rectangle(3, 3)
        test1 = str(obj1)
        self.assertTrue(test1[:50], '<models.rectangle.Rectangle object at ')
        self.assertTrue(obj1.id, 1)

        obj2 = Rectangle(3, 3, 1, 1, 420)
        test2 = str(obj2)
        self.assertTrue(test2[:50], '<models.rectangle.Rectangle object at ')
        self.assertTrue(obj2.id, 420)

        obj3 = Rectangle(3, 3)
        test3 = str(obj3)
        self.assertTrue(test3[:50], '<models.rectangle.Rectangle object at ')
        self.assertTrue(obj3.id, 2)

    def test_rect_id(self):
        """
        Test that id of rectangle objects is being counted/stored properly
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 33, 5)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(3, 33, 5, 6)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(3, 33, 5, 6, 19)
        self.assertEqual(r4.id, 19)
        r5 = Rectangle(3, 33, 5, 6, 11)
        self.assertEqual(r5.id, 11)
        r6 = Rectangle(3, 33, 5, 6, -2)
        self.assertEqual(r6.id, -2)

    def test_argument_number(self):
        """
        Test the number of arguments passed to Rectangle class
        ...should all raise TypeError
        """
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(4)
            Rectangle(x=1, y=2)

    def test_area_method(self):
        """
        Testing the area method of Rectangle with integers that
        should not raise any exception errors
        """
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 7, 3, 2)
        r4 = Rectangle(9320843029, 2103720913)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 4 * 5)
        self.assertEqual(r3.area(), 6 * 7)
        self.assertEqual(r4.area(), 9320843029 * 2103720913)

    def test_area_args(self):
        """
        Test the number of arguments of the method area
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            self.rect1.area(1)

    def test_rect_TypeError_width(self):
        """
        Test for width argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('string', 2)
            Rectangle(None, 2)
            Rectangle(True, 1)
            Rectangle((3, 4), 2)
            Rectangle(float('nan'), 2)
            Rectangle(float('inf'), 2)

    def test_rect_TypeError_height(self):
        """
        Test for height argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 'string')
            Rectangle(2, None)
            Rectangle(1, True)
            Rectangle(2, (3, 4))
            Rectangle(2, float('nan'))
            Rectangle(2, float('inf'))

    def test_rect_TypeError_x(self):
        """
        Test for x argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 'string')
            Rectangle(2, 3, None)
            Rectangle(1, 3, True)
            Rectangle(2, 3, (3, 4))
            Rectangle(2, 3, float('nan'))
            Rectangle(2, 3, float('inf'))

    def test_rect_TypeError_y(self):
        """
        Test for y argument TypeError
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 3, 'string')
            Rectangle(2, 3, 5, None)
            Rectangle(1, 3, 3, True)
            Rectangle(2, 3, 6, (3, 4))
            Rectangle(2, 3, 2, float('nan'))
            Rectangle(2, 3, 7, float('inf'))

    def test_rect_ValueError_height(self):
        """
        Test for height ValueError
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -4)
            Rectangle(3, 0)
            Rectangle(width=2)

    def test_rect_ValueError_width(self):
        """
        Test for width ValueError
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 2)
            Rectangle(0, 6)
            Rectangle(height=2)

    def test_rect_ValueError_x(self):
        """
        Test for x ValueError
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 5, -2)
            Rectangle(5, 4, 0)

    def test_rect_ValueError_y(self):
        """
        Test for y ValueError
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 3, -2)
            Rectangle(5, 4, 4, 0)

    def test_rect_str(self):
        """
        Test that str method for Rectangle class prints correct string format
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (9) 2/2 - 2/3")
        r2 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 2/2 - 2/3")

    def test_rect_to_dictionary(self):
        """
        Test that to_dictionary method for Rectangle class works
        """
        r1 = Rectangle(2, 4, 1, 1, 7)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 1, 'id': 7,
                                              'height': 4, 'width': 2})

    def test_rect_update(self):
        """
        Test that update method for Rectangle class works
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        stringrep = str(r1)
        self.assertEqual(stringrep, "[Rectangle] (1) 10/10 - 10/1")

if __name__ == '__main__':
    unittest.main()
