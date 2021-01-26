#!/usr/bin/python3
""" This module contains a class Square that
    inherits from Rectangle class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init method
        Args:
            self
            size: size of a side of the square
            x: position on x axis
            y: position on y axis
            id: we can assume id is an integer, and we
                don't need to test the type of it
                - default value of id is set to None
        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        #  use init method from Rectangle, but pass in size for width & height

    def __str__(self):
        """ __str method:
        Args: self
        Return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """ getter for size
        Returns:
            size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ property setter for size
        Args:
            value: integer
        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        Returns:
            None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method: assigns a key/value argument to attributes
            for *args:
                1st argument should be id attribute
                2nd argument should be size attribute
                3rd argument should be x attribute
                4th argument should be y attribute
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
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ to_dictionary method:
        Args: self
        Return: the dictionary representation of a Square
                the dictionary contains: id, size, x, and y
        """
        mySquare = {}
        mySquare["id"] = self.id
        mySquare["size"] = self.size
        mySquare["x"] = self.x
        mySquare["y"] = self.y

        return mySquare
