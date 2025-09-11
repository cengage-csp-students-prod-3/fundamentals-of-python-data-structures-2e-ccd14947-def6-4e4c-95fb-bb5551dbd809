"""
File: expressiontree.py
Project 10.9

Reuse your solution from Programming Exercise 10.8 as your starter file
"""

from tokens import Token

    # Reuse your solution from Programming Exercise 10.8 as your starter file

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('^'), c, b)
    print("Expect ((4 * (2 + 3) ^ (2 + 3)):", c.infix())
    print("Expect ^ * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + ^       :", c.postfix())
    print("Expect 3200000                 :", c.value())

if __name__ == "__main__":
    main()




