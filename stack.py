# SWDV 610: Data Structures and Algorithms
# Linked list based implementation of a stack class

class Stack:
    """A linked list implementation of a stack"""

    class _Node:
        """Nonpublic class for a singly linked list node"""
        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size
    
    def is_empty(self):
        return self.size() == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return False
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        return answer
    
    def top(self):
        if self.is_empty():
            return False
        
        return self._head._element
    
if __name__ == '__main__':
    s = Stack()
    s.push(7)
    s.push(8)
    s.push(9)

    print('size:', s.size())        # -> 3
    print('top:', s.top(), '\n')    # -> 9

    print(s.pop())                  # -> 9
    s.push(27)
    print(s.pop())                  # -> 27
    print(s.pop())                  # -> 8
    print(s.pop())                  # -> 7
    print(s.pop())                  # -> False
