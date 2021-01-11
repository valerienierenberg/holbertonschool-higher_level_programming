#!/usr/bin/python3
""" This module contains a class Rectangle """


class Rectangle:
    """ Rectangle class - represents a rectangle

    Attributes:
        number_of_instances: incremented during each new instance instantiation
                            and decremented during each instance deletion
        __height: integer, height of rectangle
        __width: integer, width of rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init method
        Args:
            size: integer
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter for __width
        Returns:
            width of square
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter 'width'
        Args:
            value: integer
        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height
        Returns:
            height of square
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter 'height'
        Args:
            value: integer
        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ area method
        Args:
            self: rectangle object
        Return:
            the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter method
        Args:
            self: rectangle object
        Return:
            the current rectangle area
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ __str method:
        Args: self
        Return: rectangle printed with "#"
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for x in range(self.height):
            for y in range(self.width):
                output += str(self.print_symbol)
            if x == self.height - 1:
                break
            else:
                output += '\n'
        return output

    def __repr__(self):
        """ __repr method:
        Args: self
        Return: string representation of rectangle that allows recreation
        of a new instance by using eval()
        """
        return "Rectangle({}, {})".format(
            eval(str(self.width)), eval(str(self.height)))

    def __del__(self):
        """ __del method:
        Args: self
        Return: none
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        r1area = Rectangle.area(rect_1)
        r2area = Rectangle.area(rect_2)
        if r1area == r2area or r1area > r2area:
            return rect_1
        if r1area < r2area:
            return rect_2

    @classmethod
    def square(cls, size=0):
        a = Rectangle()
        a.__width = size
        a.__height = size
        return a
