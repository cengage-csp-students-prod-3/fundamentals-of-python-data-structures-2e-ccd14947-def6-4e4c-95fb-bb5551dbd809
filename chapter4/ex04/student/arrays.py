"""
File: arrays.py
Project 4.4

Adds methods insert and pop to insert or remove an item
at a given position in the array.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = Array(<capacity>, <optional fill value>)

The fill value is None by default..
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.logicalSize = 0
        self.fillValue = fillValue
        self.items = [fillValue] * capacity

    def size(self):
        """Return the logical size (number of actual elements)."""
        return self.logicalSize

    def __len__(self):
        """Return the physical size (capacity)."""
        return len(self.items)

    def __str__(self):
        """String representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

    def grow(self):
        """Double the physical size of the array."""
        temp = Array(len(self) * 2, self.fillValue)
        for i in range(self.logicalSize):
            temp[i] = self.items[i]
        self.items = temp.items

    def shrink(self):
        """Halve the physical size of the array."""
        temp = Array(len(self) // 2, self.fillValue)
        for i in range(self.logicalSize):
            temp[i] = self.items[i]
        self.items = temp.items

    def insert(self, position, item):
        """Insert item at the given position.
        If position >= logicalSize, insert at the end."""
        # Grow if full
        if self.logicalSize == len(self.items):
            self.grow()

        # Clamp position
        if position > self.logicalSize:
            position = self.logicalSize

        # Shift right
        for i in range(self.logicalSize, position, -1):
            self.items[i] = self.items[i - 1]

        self.items[position] = item
        self.logicalSize += 1

    def pop(self, position):
        """Remove and return the item at the given position.
        Precondition: 0 <= position < size()."""
        if position < 0 or position >= self.logicalSize:
            raise IndexError("Index out of range")

        item = self.items[position]

        # Shift left
        for i in range(position, self.logicalSize - 1):
            self.items[i] = self.items[i + 1]

        # Reset vacated cell
        self.items[self.logicalSize - 1] = self.fillValue
        self.logicalSize -= 1

        return item


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)

    for item in range(4):
        a.insert(0, item)
    print("Items:", a)

    a.insert(1, 77)
    print("Items:", a)

    a.insert(10, 10)
    print("Items:", a)

    print(a.pop(3))
    print("Items:", a)

    for count in range(a.size()):
        print(a.pop(0), end=" ")
    print()


if __name__ == "__main__":
    main()
