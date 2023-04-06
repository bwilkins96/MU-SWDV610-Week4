# SWDV 610: Data Structures and Algorithms
# Simple stack implementation using a list

class Stack:
    """A list-based implementation of a stack that accepts only unique values"""

    def __init__(self):
        self._stack = []

    def push(self, data):
        if data not in self._stack:
            self._stack.append(data)
            return True
        
        return False
    
    def pop(self):
        if len(self._stack) <= 0:
            return 'Stack empty!'
        
        return self._stack.pop()
    
    def size(self):
        return len(self._stack)
    
if __name__ == '__main__':
    s = Stack()
    print(s.push(5))
    print(s.push(9))
    print(s.push(6))
    print(s.push(5))

    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.pop())
