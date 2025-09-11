"""
File: arrayqueue.py
Project 8.2
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.front = self.rear = -1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while cursor != self.rear:
            yield self.items[cursor]
            if cursor == len(self.items) - 1:
                cursor = 0
            else:
                cursor += 1
        if cursor == self.rear and cursor != -1:
            yield self.items[cursor]
    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self.items[self.front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        pass
    
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        return None        
         
