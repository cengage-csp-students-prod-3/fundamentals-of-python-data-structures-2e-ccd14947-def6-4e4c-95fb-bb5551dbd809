"""
File: scanner.py
A scanner for processing languages.

Reuse your solution from Programming Exercise 7.3 as your starter file
"""

from tokens import Token

class Scanner(object):

    EOE = ';'        # end-of-expression
    TAB = '\t'       # tab

    # Reuse your solution from Programming Exercise 7.3 as your starter file


def main():
    # A simple tester program
    while True:
        sourceStr = input("Enter an expression: ")
        if sourceStr == "": break
        scanner = Scanner(sourceStr)
        while scanner.hasNext():
            print(scanner.next())

if __name__ == '__main__': 
    main()

