"""
File: lisplist.py
Project 9.10

Adds lispMap and lispFilter functions for Lisp lists.
"""

class Node(object):
    """Represents a singly linked node."""

    # def listMap(self):

    # def lispFilter(self):


    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Returns the string representation of a nonempty lisp list."""
        def buildString(lyst):
            if isEmpty(rest(lyst)):
                return str(first(lyst))
            else:
                return str(first(lyst)) + " " + buildString(rest(lyst))

        return "(" + buildString(self) + ")"

THE_EMPTY_LIST = None

# Basic functions

def isEmpty(lyst):
    """Returns True if lyst is empty or False otherwise."""
    return lyst is THE_EMPTY_LIST

def first(lyst):
    """Returns the item at the head of lyst.
    Precondition: lyst is not empty."""
    return lyst.data

def rest(lyst):
    """Returns a list of items in lyst, after the first one.
    Precondition: lyst is not empty."""
    return lyst.next

def cons(item, lyst):
    """Adds item to the head of lyst and
    returns the resulting list."""
    return Node(item, lyst)

# Auxiliary functions

def contains(item, lyst):
    """Returns True if item is in lyst or
    False otherwise."""
    if isEmpty(lyst):
        return False
    elif item == first(lyst):
        return True
    else:
        return contains(item, rest(lyst))

def get(index, lyst):
    """Returns the item at position index in lyst.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return first(lyst)
    else:
        return get(index - 1, rest(lyst))

def length(lyst):
    """Returns the number of items in lyst."""
    if isEmpty(lyst): return 0
    else: return 1 + length(rest(lyst))
    
def buildRange(lower, upper):
    """Returns a list containing the numbers from
    lower through upper.
    Precondition: lower <= upper"""
    if lower == upper:
        return cons(lower, THE_EMPTY_LIST)
    else:
        return cons(lower, buildRange(lower + 1, upper))

def lispMap(fn, lyst):
    """Applies fn to each element of lyst, returning a new Lisp list."""
    if isEmpty(lyst):
        return None
    else:
        return cons(fn(first(lyst)), lispMap(fn, rest(lyst)))

def lispFilter(predicate, lyst):
    """Returns a Lisp list of elements that satisfy predicate."""
    if isEmpty(lyst):
        return None
    elif predicate(first(lyst)):
        return cons(first(lyst), lispFilter(predicate, rest(lyst)))
    else:
        return lispFilter(predicate, rest(lyst))


def remove(index, lyst):
    """Returns a list with the item at index removed.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return rest(lyst)
    else:
        return cons(first(lyst),
                    remove(index - 1, rest(lyst)))

def removeAll(item, lyst):
    if item ==  lyst([0]):
        return remove

def insert(index, item, lyst):
    """Returns a list with the item inserted at index.
    Precondition: 0 <= index < length(lyst)"""
    return lyst(index(item))

def equals(lyst1, lyst2):
    """Two lists are equal if they are both empty"""
    if not lyst1 and not lyst2: 
        return True

    """Two lists are not equal if one is empty"""
    if not lyst1 or not lyst2: 
        return False

    """Two list are equal if lengths of the lists are the same, 
    their first items are equal and the rest of their items are equal."""
    return lyst1[0] == lyst2[0] and equals(lyst1[1:], lyst2[1:]) 

def main(): # type: ignore
    """Create a list with 9..0 and print it."""
    lyst = THE_EMPTY_LIST
    for i in range(10):
        lyst = cons(i, lyst)
    print("List =", lyst)
    print("Length =", length(lyst))

if __name__ == "__main__":
    main()
        
