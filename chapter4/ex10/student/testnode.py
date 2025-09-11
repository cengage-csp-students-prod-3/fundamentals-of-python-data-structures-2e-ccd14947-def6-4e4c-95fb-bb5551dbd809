"""
File: testnode.py
Project 4.10

Add a remove function.

Tests the Node class.

Reuse your solution from Programming Exercise 4.9 as your starter file
"""

from node import Node

# Reuse your solution from Programming Exercise 4.9 as your starter file

def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("1:", end = " ")
    printStructure(head)

    (head, item) = pop(0, head)
    print("1:", item, end = " ")
    printStructure(head)

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    
    (head, item) = pop(0, head)
    print("5 4 3 2 1:", item, end = " ")
    printStructure(head)
    
    (head, item) = pop(length(head) - 1, head)
    print("1 4 3 2:", item, end = " ")
    printStructure(head)

    (head, item) = pop(1, head)
    print("3 4 2:", item, end = " ")
    printStructure(head)

    pop(4, head)
    
if __name__ == "__main__": main()