#!usr/bin/python3
class Square:
    """ Square class """
    def __init__(self, size=0):
        """ __init method
        Args:
            size: integer
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ property setter 'size'
        Args:
            value: integer
        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

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
        if self.size == 0:
            print()
        for x in range(self.size):
            for y in range(self.size):
                    print("#", end="")
            print()
