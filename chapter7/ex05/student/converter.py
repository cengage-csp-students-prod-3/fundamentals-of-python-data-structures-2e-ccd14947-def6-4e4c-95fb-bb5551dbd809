"""
File: converter.py
Project 7.5

Defines a class that converts infix expressions to postfix form.
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def convert(self):
        """Returns a list of tokens that represent the postfix
        form.  Assumes that the infix expression is syntactically correct"""
        postfix = []
        stack = ArrayStack()
        while self.scanner.hasNext():
            currentToken = self.scanner.next()
            if currentToken.getType() == Token.INT:
                postfix.append(currentToken)
            else:
                # Write your code here
        
		while not stack.isEmpty():
            postfix.append(stack.pop())
        return postfix
   

def main():
    while True:
        # Write your code here

if __name__ == "__main__":
    main()


