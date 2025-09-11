"""
File: converter.py
Project 7.8
Add error recovery to the infix to postfix converter.
Defines a class that converts infix expressions to postfix form.

Reuse your solution from Programming Exercise 7.7 as your starter file
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

	# Reuse your solution from Programming Exercise 7.7 as your starter file

    def __init__(self, scanner):
        self.expressionSoFar = ""
        self.operatorStack = ArrayStack()
        self.scanner = scanner


    def convert(self):
        """Returns a list of tokens that represent the postfix
        form of sourceStr.  Assumes that the infix expression
        in sourceStr is syntactically correct"""
       # Add from exercise 7
   
    def __str__(self):
        # Add from exercise 7

    def conversionStatus(self):
        # Add from exercise 7

    
def main():
    while True:
        # Add from exercise 7

if __name__ == "__main__":
    main()
