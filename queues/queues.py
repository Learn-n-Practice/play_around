from collections import deque
from heapq import heappush, heappop
from itertools import count


class IterableMixin:
    "A mixin class to create an iterable and length reporting"

    def __len__(self):
        """Enable length reporting"""
        return len(self._elements)

    def __iter__(self):
        """Make the queue iterable"""
        while len(self) > 0:
            yield self.pop()


class Queue(IterableMixin):
    """A class that implements a queue (FIFO Queue)"""

    def __init__(self, *elements):
        self._elements = deque(*elements)

    def push(self, element):
        """Add element to end of queue"""
        self._elements.append(element)

    def pop(self):
        """Remove element from queue"""
        return self._elements.popleft()


class Stack(Queue):
    """A class that implements a stack (LIFO Queue). It inherits the Queue class"""

    def pop(self):
        return self._elements.pop()


class PriorityQueue(IterableMixin):
    """A class that implements a priority queue"""

    def __init__(self):
        self._elements = []
        self._counter = count()

    def push(self, priority, value):
        heappush(self._elements, (-priority, next(self._counter), value))

    def pop(self):
        return heappop(self._elements)[-1]
