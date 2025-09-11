"""
File: treesortedset.py
Project 11.8

A tree-based sorted set implementation.
"""

from linkedbst import LinkedBST
from abstractset import AbstractSet

class TreeSortedSet(AbstractSet):
    """An tree-based sorted set implementation."""

    def __init__(self, sourceCollection = None):
        self.items = LinkedBST(sourceCollection)

    def __iter__(self):
        """Supports an inorder traversal on a view of self."""
        return self.items.inorder()

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        result = type(self)(self)
        for item in self:
            result.add(item)
        return result

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        return item in self.items

    # Remaining methods are exercises
