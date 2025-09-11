"""
File: hashset.py
Project 11.6

Adjusts the array's capacity and rehashes if the load factor > .8 after creating
the HashSet.
"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractSet, AbstractCollection):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None,
                 capacity = None):
        if capacity is None:
            self.capacity = HashSet.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self.index = abs(hash(item)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]
        while self.foundNode != None:
            if self.foundNode.data == item: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    # Methods __str__(), __iter__() and remove() are exercises.

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.foundNode = self.priorNode = None
        self.index = -1
        self.array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self: 
            self.array[self.index] = Node(item,
                                          self.array[self.index])
            self.size += 1
