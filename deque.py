# SWDV 610: Data Structures and Algorithms
# Linked list based implementation of a deque class

class Deque:
    """A linked list implementation of a deque"""

    class _Node:
        """Nonpublic class for a doubly linked list node"""
        def __init__(self, element, next=None, prev=None):
            self._element = element
            self._next = next
            self._prev = prev