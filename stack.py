# SWDV 610: Data Structures and Algorithms
# Linked list based implementation of a stack class

class Stack:
    """A linked list implementation of a stack"""

    class _Node:
        """Nonpublic class for a singly linked list node"""
        def __init__(self, element, next=None):
            self._element = element
            self._next = next