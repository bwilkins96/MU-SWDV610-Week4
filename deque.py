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

    def __init__(self):
        """Initializes an empty deque"""
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        """Returns the size of the deque"""
        return self._size
    
    def is_empty(self):
        """Returns whether the deque is empty"""
        return self.size() == 0
    
    def add_front(self, element):
        """Adds a node containing the element to the head of the deque"""
        new_node = self._Node(element, self._head)

        if self.is_empty():
            self._tail = new_node
        else: 
            self._head._prev = new_node
        
        self._head = new_node
        self._size += 1

    def add_rear(self, element):
        """Adds a node containing the element to the tail of the deque"""
        new_node = self._Node(element)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail

        self._tail = new_node
        self._size += 1

    def pop_front(self):
        """Returns the element in the head node and removes the node"""
        if self.is_empty():
            return None
        
        answer = self._head._element
        if self.size() == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
            self._head._prev = None

        self._size -= 1
        return answer

    def pop_rear(self):
        """Returns the element in the tail node and removes the node"""
        if self.is_empty():
            return None
        
        answer = self._tail._element
        if self.size() == 1:
            self._head = None
            self._tail = None
        else:  
            self._tail = self._tail._prev
            self._tail._next = None

        self._size -= 1
        return answer

    def front(self):
        """Returns the element in the head node without removing the node"""
        if self.is_empty():
            return None
        
        return self._head._element

    def rear(self):
        """Returns the element in the tail node without removing the node"""
        if self.is_empty():
            return None
        
        return self._tail._element
    
    def print_deque(self):
        """Prints the elements in the deque, in forward order"""
        current = self._head

        while current:
            print(current._element, end='')
            current = current._next
            if current: print(', ', end='')
        
        print()

    def print_deque_reverse(self):
        """Prints the elements in the deque, in reverse order"""
        current = self._tail
        
        while current:
            print(current._element, end='')
            current = current._prev
            if current: print(', ', end='')
        
        print()

if __name__ == '__main__':
    d = Deque()
    d.add_front(1)
    d.add_front(2)
    d.add_rear('A')
    d.add_rear('B')

    d.print_deque()                  # -> 2, 1, A, B
    d.print_deque_reverse()          # -> B, A, 1, 2
    print('size:', d.size())         # -> 4
    print('front:', d.front())       # -> 2
    print('rear:', d.rear(), '\n')   # -> B
   
    print(d.pop_front())             # -> 2
    print(d.pop_front())             # -> 1
    d.add_rear('hello world!')       
    print(d.pop_rear())              # -> hello world!
    print(d.pop_rear())              # -> B
    print(d.pop_front())             # -> A
    print(d.pop_rear())              # -> None




    
