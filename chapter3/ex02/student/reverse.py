
"""
File: reverse.py
Project 3.2
Defines a function to reverse the elements in a list.
Computational complexity:
"""

def reverse(lyst, myList): 
    """Reverses the elements in a list in linear time."""
    # Use indexes to the first and last element
    # and move them toward each other.
    
 
    for item in lyst:
        myList.insert(0,lyst[item])

def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    
def main():
    """Tests with two lists."""
    lyst = list(range(4))
    myList = []
    reverse(lyst, myList)
    print(myList)
    myList.clear()
    lyst = list(range(3))
    reverse(lyst, myList)
    print(myList)

if __name__ == "__main__":
    main()

    
