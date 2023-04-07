# SWDV 610: Data Structures and Algorithms
# Linked list based implementation of a queue class

class Queue:
    """A linked list implementation of a queue"""

    class _Node:
        """Nonpublic class for a singly linked list node"""
        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        """Initializes an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        """Returns the size of the queue"""
        return self._size
    
    def is_empty(self):
        """Returns whether the queue is empty"""
        return self.size() == 0
    
    def enqueue(self, element):
        """Adds a node containing the element to the tail of the queue"""
        new_node = self._Node(element)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Returns the element in the head node and removes the node"""
        if self.is_empty():
            return None
        
        answer = self._head._element
        if self.size() == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next 

        self._size -= 1
        return answer
    
    def front(self):
        """Returns the element in the head node without removing the node"""
        if self.is_empty():
            return None
        
        return self._head._element
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    print('size:', q.size())            # -> 2
    print('front:', q.front(), '\n')    # -> 1

    print(q.dequeue())                  # -> 1
    q.enqueue(3)                       
    print(q.dequeue())                  # -> 2
    print(q.dequeue())                  # -> 3
    print(q.dequeue())                  # -> None
