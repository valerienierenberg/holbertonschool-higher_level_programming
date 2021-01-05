#!/usr/bin/python3
""" This module contains a class Square """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ __init method
        Args:
            size: integer
            position: tuple of integers
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter for __size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ property setter 'size'
        Args:
            value: integer
        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ getter for __position
        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ property setter 'position'
        Args:
            value: tuple of integers
        Raises:
            TypeError: if tuple is not two positive ints
        """
        if len(value) == 1 or type(value) != tuple or type(value[0]) is not \
                int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ area method
        Args:
            self: square object
        Return:
            the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ my_print method
        Args:
            self: square object
        Description:
            prints in stdout the square with the character #
        """
        if self.size == 0 or self.position[1] > 0:
            print()
        for x in range(self.size):
            print("{}{}".format(' ' * self.position[0], '#' * self.size))
