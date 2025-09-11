"""
File: arrays.py
Project 4.6

Drops __iter__ and modifies __str__.  The user of an array
should only be able to see the items currently available in it.
The user can use an index-based loop over its logical size
to visit the items currently available in the array.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Reuse your solution from Programming Exercise 4.5 as your starter file
"""

class Array(object):
    """Represents an array."""
	
	# Reuse your solution from Programming Exercise 4.5 as your starter file

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

def main():
    """Test code for modified Array class."""
    a = Array(10)
    for item in range(4):
        a.insert(0, item)
    print(a)
    
if __name__ == "__main__":
    main()