"""
File: linkedbag.py
Project 6.2
Author: Ken Lambert
"""

from node import Node
from abstractbag import AbstractBag

class LinkedBag(object):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """-Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    # Mutator methods

    def add(self, item):
        """Adds item to self."""
        self.items = Node(item, self.items)
        self.size += 1

   