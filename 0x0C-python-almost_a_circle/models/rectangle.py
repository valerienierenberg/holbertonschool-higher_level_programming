#!/usr/bin/python3
""" This module contains a class Rectangle that
    inherits from Base class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init method
        Args:
            self
            width: width of rectangle, integer
            height: height of rectangle, integer
            x: position on x axis
            y: position on y axis
            id: we can assume id is an integer, and we
                don't need to test the type of it
                - default value of id is set to None
        Returns:
            None
        """
        super().__init__(id)  # get the Base init method and add on below
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for __width
        Returns:
            width of rectangle
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
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height
        Returns:
            height of rectangle
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
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for __x
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ property setter 'x'
        Args:
            value: integer
        Raises:
            TypeError: if x is not an int
            ValueError: if x is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for __y
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ property setter 'y'
        Args:
            value: integer
        Raises:
            TypeError: if y is not an int
            ValueError: if y is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ area method:
            Attributes: self
            Returns: area of rectangle
        """
        return self.__width * self.__height
        # return ("{}".format(self.__width * self.__height))  --- another way

    def display(self):
        """ display method:
        Args: self
        Prints: rectangle printed with "#"
        Returns: prints - y = "\n" x = " ", size of rectangle - "#"
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        print("\n" * self.__y, end="")
        for a in range(self.__height):
            print(" " * self.__x, end="")
            for h in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ __str method:
        Args: self
        Return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update method: assigns a key/value argument to attributes
            for *args:
                1st argument should be id attribute
                2nd argument should be width attribute
                3rd argument should be height attribute
                4th argument should be x attribute
                5th argument should be y attribute
            for **kwargs:
                argument order is not important
        Args: self
              *args - variable number of arguments
              **kwargs - variable number of keyword arguments
        Return: None
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ to_dictionary method:
        Args: self
        Return: the dictionary representation of a Rectangle
                the dictionary contains: id, width, height, x, and y
        """
        myRect = {}
        myRect["id"] = self.id  # set key "id" equal to value of id attribute
        myRect["width"] = self.width
        myRect["height"] = self.height
        myRect["x"] = self.x
        myRect["y"] = self.y

        return myRect
