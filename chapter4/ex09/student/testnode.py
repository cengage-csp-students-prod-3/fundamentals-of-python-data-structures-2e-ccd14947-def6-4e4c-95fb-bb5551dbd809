"""
File: testnode.py
Project 4.9

Add an insert function.

Tests the Node class.

Reuse your solution from Programming Exercise 4.8 as your starter file
"""

from node import Node

# Reuse your solution from Programming Exercise 4.8 as your starter file

def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("1:", end = " ")
    printStructure(head)

    head = insert(1, "2", head)
    print("1 2:", end = " ")
    printStructure(head)

    head = insert(0, "0", head)
    print("0 1 2:", end = " ")
    printStructure(head)

    head = insert(3, "3", head)
    print("0 1 2 3:", end = " ")
    printStructure(head)

    head = insert(1, "9", head)
    print("0 9 1 2 3:", end = " ")
    printStructure(head)

if __name__ == "__main__": main()
