# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/26/2022
# Description: linked list assignment changing iterative functions to recursive.
#


class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self._head = None

    #def get_head(self):
    #    return self._head

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
            return
        self.rec_add(self._head, val)

    def rec_add(self, node, val):
        """ Adds a node containing val to the linked list"""

        if node.next is None:
            node.next = Node(val)
            return
        self.rec_add(node.next, val)
        return

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
            return
        self.rec_remove(self._head, val)

    def rec_remove(self, node, val):
        """Removes the node containing val from the linked list"""

        if node.next is None:
            return

        if node.next.data == val:
            node.next = node.next.next
            return
        self.rec_remove(node.next, val)

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def to_plain_list(self):
        """
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        if self._head is None:
            return result
        return self.rec_to_plain_list(self._head, result)


    def rec_to_plain_list(self, node, result):
        """Returns a regular Python list containing the same values, in the same order, as the linked list"""
        if node is None:
            return result

        if node is not None:
            result += [node.data]
            node = node.next
            self.rec_to_plain_list(node, result)
        return result

    def insert(self, val, pos):
        """insert method takes as parameters a value and a position (in that order)."""

        if self._head is None:
           self.add(val)
           return

        if pos == 0:
            temp = self._head.next
            self._head = Node(val)
            self._head.next = temp
        self.rec_insert(self._head, val, pos)

    def rec_insert(self,node, val, pos):
        """insert method takes as parameters a value and a position (in that order)."""

        if node.next is None:
            node.next =Node(val)
            return

        if pos == 1:
            temp = node.next
            node.next = Node(val)
            node.next.next = temp
            return
        self.rec_insert(node.next, val, pos - 1)
        return

    def reverse(self):
        """Reverses the linked list"""
        current = self._head
        previous = None
        self.rec_reverse(current, previous)

    def rec_reverse(self, current, previous):
        """Reverses the linked list"""
        if current is None:
            self._head = previous
            return
        following = current.next
        current.next = previous
        previous = current
        current = following
        self.rec_reverse(current, previous)
        return

    def contains(self, key):
        """
        Returns True if the list contains a Node with the value key,
        otherwise returns False
        """
        if self._head is None:  # If the list is empty
            return False
        return self.rec_contains(key, self._head)

    def rec_contains(self, val, node):
        """
        Returns True if the list contains a Node with the value key,
        otherwise returns False
        """
        if node is not None:
            if node.data == val:
                return True
            return self.rec_contains(val, node.next)

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)


