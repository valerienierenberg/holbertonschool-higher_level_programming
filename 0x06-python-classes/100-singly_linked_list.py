#!usr/bin/python3
class Node:
    """ Node class """
    def __init__(self, data, next_node=None):
        """ __init method
        Args:
            size: integer
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """ property setter 'data'
        Args:
            value: integer
        Raises:
            TypeError: if size is not an int
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ property setter 'next_node'
        Args:
            value: Node
        Raises:
            TypeError: if next_node is not None or a Node
        """
        if type(value) is not Node and not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ SinglyLinkedList class """
    def __init__(self):
        """ __init method
        Args:
            self
        """
        self.__head = None

    def sorted_insert(self, value):
        value = value

# UNFINISHED....
