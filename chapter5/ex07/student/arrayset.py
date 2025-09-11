"""
Project 5.7
File: arrayset.py
Author: Ken Lambert
"""

from arrays import Array

class ArraySet(object):
    """An array-based set implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArraySet.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        # Add from exercise 6
    
    def __len__(self):
        """Returns the number of items in self."""
        # Add from exercise 6

    def __str__(self):
        """Returns the string representation of self."""
        # Add from exercise 6

    def __iter__(self):
        """Supports iteration over a view of self."""
        # Add from exercise 6

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        # Add from exercise 6

    def clone(self):
        """Returns a copy of self."""
        # Add from exercise 6

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        # Add from exercise 6

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Add from exercise 6

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Add from exercise 6
       
        
