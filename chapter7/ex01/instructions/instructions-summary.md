In this exercise you'll be completing an array-based and a link-based `stack` collection type discussed in this chapter. Both have similar implementations, but a link-based stack uses nodes and an array-based stack can resize the array if necessary.

In the `LinkedStack` class of the *linkedstack.py* file, complete the following:
1. Complete the implementation of the constructor method.
	- `__init__`, sets the initial state of self, which includes the contents of sourceCollection, if it's present.
2. Complete the implementation of the accessor methods.
	- `__iter__`, supports iteration over a view of self and visits items from bottom to top of stack.
	- `peek()`, returns the item at the top of the stack.
		- Precondition: the stack is not empty.
        - Raises: KeyError if the stack is empty.
3. Complete the implementation of the mutator methods.
	- `clear()`, makes self become empty.
	- `push()`, adds item to the top of the stack.
	- `pop()`, removes and returns the item at the top of the stack.
        - Precondition: the stack is not empty.
        - Raises: KeyError if the stack is empty.
        - Postcondition: the top item is removed from the stack.

In the `ArrayStack` class of the *arraystack.py* file, complete the following:
1. Complete the implementation of the constructor method.
	- `__init__`, sets the initial state of self, which includes the contents of sourceCollection, if it's present.
2. Complete the implementation of the accessor methods.
	- `__iter__`, supports iteration over a view of self and visits items from bottom to top of stack.
	- `peek()`, returns the item at the top of the stack.
		- Precondition: the stack is not empty.
        - Raises: KeyError if the stack is empty.
3. Complete the implementation of the mutator methods.
	- `clear()`, makes self become empty.
	- `push()`, adds item to the top of the stack.
	- `pop()`, removes and returns the item at the top of the stack.
        - Precondition: the stack is not empty.
        - Raises: KeyError if the stack is empty.
        - Postcondition: the top item is removed from the stack.
		
Verify that exceptions are raised when __preconditions__ are violated and that the array-based implementation adds or removes storage as needed.

To test your program run the `test()` method in the *teststack.py* file.

Your program's output should look like the following:

```
Testing <class 'arraystack.ArrayStack'>
Length: 0
Empty: True
Push 1-10
Peeking: 10
Items (bottom to top): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Length: 10
Empty: False
Items in clone (bottom to top): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Length of clone after clear: 0
Push 11
Popping items (top to bottom): 11 10 9 8 7 6 5 4 3 2 1 
Length: 0
Empty: True
Testing <class 'linkedstack.LinkedStack'>
Length: 0
Empty: True
Push 1-10
Peeking: 10
Items (bottom to top): Traceback (most recent call last):
  File "teststack.py", line 38, in <module>
    test(LinkedStack)
  File "teststack.py", line 21, in test
    print("Items (bottom to top):",  s)
  File "/root/sandbox/abstractcollection.py", line 29, in __str__
    return "[" + ", ".join(map(str, self)) + "]"
TypeError: iter() returned non-iterator of type 'NoneType'
```