from collections import deque
from heapq import heappush, heappop

class Queue:
    """A class that implements a queue (FIFO Queue)"""
    
    def __init__(self):
        self._elements = deque()

    def __len__(self):
        """Enable length reporting"""
        return len(self._elements)

    def __iter__(self):
        """Make the queue iterable"""
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        """Add element to end of queue"""
        self._elements.append(element)

    def dequeue(self):
        """Remove element from queue"""
        return self._elements.popleft()


class Stack(Queue):
    """A class that implements a stack (LIFO Queue). It inherits the Queue class"""

    def dequeue(self):
        return self._elements.pop()


class PriorityQueue:
    """A class that implements a priority queue"""

    def __init__(self):
        self._queue = []
    
    def push(self, priority, value):
        heappush(self._queue, (-priority, value))
    
    def pop(self):
        return heappop(self._queue)[1]