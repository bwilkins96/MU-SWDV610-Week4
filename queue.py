# SWDV 610: Data Structures and Algorithms
# Linked list based implementation of a queue class

class Queue:
    """A linked list implementation of a queue"""

    class _Node:
        """Nonpublic class for a singly linked list node"""
        def __init__(self, element, next=None):
            self._element = element
            self._next = next