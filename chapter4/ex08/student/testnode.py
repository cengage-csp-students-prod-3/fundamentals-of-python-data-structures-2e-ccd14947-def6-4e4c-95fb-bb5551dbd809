"""
File: testnode.py
Project 4.8

Add a length function.

Tests the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    # Write your code here
    

def main():
    """Tests modifications."""
    head = None
    print("0:", length(head))

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)

    print("5:", length(head))

if __name__ == "__main__": main()
