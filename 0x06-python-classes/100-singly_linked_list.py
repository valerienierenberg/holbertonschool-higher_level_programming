#!/usr/bin/python3
""" This module contains a class Node """


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
        """ getter for __data
        Returns:
            data of node
        """
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
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter for __next_node
        Returns:
            next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ property setter 'next_node'
        Args:
            value: Node
        Raises:
            TypeError: if next_node is not None or a Node
        """
        if type(value) is not Node and value is not None:
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
        """ sorted_insert method
        Args:
            self, value - int
        """
        newNode = Node(value)
        if self.head is None:
            self.__head = Node(value)
        if self.__head.data < value:
            newNode.next_node = self.__head
            self.__head = newNode

        # check if new_node is less than head
        # check if head is none
        # check if next_node is larger than new node
        # check if we're at end of node
        # create new node with value
        # change existing next node to point to new node and new node to
        # point to next node if exists
