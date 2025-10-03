"""
Project 5.4
File: arraybag.py
Author: Ken Lambert

Reuse your solution from Programming Exercise 5.3 as your starter file
"""

from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __getitem__(self, index):
            """Subscript operator for access at index."""
            return self.items[index]
    
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
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
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    def grow(self):
        """Double the physical size of the array."""
        temp = Array(len(self) * 2)
        for i in range(len(self)):
            temp[i] = self.items[i]
        self.items = temp.items
        
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if len(self) == len(self.items):
            self.grow()
        self.items[len(self)]=item
        self.size+=1
        # Check array memory here and increase it if necessary

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self. """
        
        # 1. Check precondition and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")

        # 2. Search for index of target item
        for i in range(len(self)):
            if self[i] == item:
                break

        # 3. Shift items to the right of target left by one position
        for j in range(i, len(self) - 1):
            self[j] = self[j + 1]

        # 4. Decrement logical size
        self.size -= 1

        # 5. Check array memory here and decrease it if necessary

            
            
            
