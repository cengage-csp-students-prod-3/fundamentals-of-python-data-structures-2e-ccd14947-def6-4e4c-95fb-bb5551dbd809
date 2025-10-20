"""
File: palindrome.py
Project 7.2

"""

from arraystack import ArrayStack

def isPalindrome(string):    
    """Returns True if string is a palindrome
    or False otherwise."""
    stack = ArrayStack()
    
    # Push each character onto the stack
    for ch in string:
        stack.push(ch)
    
    # Build reversed string by popping from the stack
    reversedString = ""
    while not stack.isEmpty():
        reversedString += stack.pop()
    
    # Compare original and reversed strings
    return string == reversedString
   

def main():
    while True:
        string = input("Enter a string or Return to quit: ")
        if string == "":
            break
        elif isPalindrome(string):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

if __name__ == '__main__': 
    main()
