"""
File: linkedqueue.py
Project 8.2
"""

from node import Node
from abstractcollection import AbstractCollection

class LinkedQueue(AbstractCollection):

    def remove(self, item):
        """Removes the first occurrence of item from the queue and
        returns it. Raises KeyError if the item is not found."""
        if self.isEmpty():
            raise KeyError(item)

        prev = None
        cursor = self.front
        while cursor is not None:
            if cursor.data == item:
                # Removing front node
                if prev is None:
                    self.front = cursor.next
                    if self.front is None:
                        # Queue is now empty
                        self.rear = None
                else:
                    prev.next = cursor.next
                    if cursor is self.rear:
                        # Removed the rear node
                        self.rear = prev

                self.size -= 1
                return item

            prev = cursor
            cursor = cursor.next

    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.front = self.rear = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    
    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        # Both front and rear pointers must be set
        # equal to None if they are cleared/empty.
        # The size should also equal 0.
        self.front = None
        self.rear = None
        self.size = 0

    
    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return oldItem
        
    