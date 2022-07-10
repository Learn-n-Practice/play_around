from collections import deque

class Queue:
    """Class that implements a queue"""
    
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        """Add element to end of queue"""
        self._elements.append(element)

    def dequeue(self):
        """Remove element from queue"""
        return self._elements.popleft()