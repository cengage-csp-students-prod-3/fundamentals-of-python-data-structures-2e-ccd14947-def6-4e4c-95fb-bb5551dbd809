Modify the maze-solving application of *Chapter 7, Exercise 9* so that it uses a queue instead of a stack.

In the `LinkedQueue` class of the *linkedqueue.py* file, complete the following:
1. Complete the implementation of the constructor:
	- `__init__` 
2. Complete the implementation of the accessor methods:
	- `__iter__`
	- `peek()`
3. Complete the implementation of the mutator methods:
	- `clear()`
	- `add()`
	- `pop()`
	
Once the queue has been setup in the *maze.py* file, complete the following:
1. Import the ```LinkedQueue``` and ```Counter``` modules from their designated files.
2. Modify the `main()` method:
	- Run each version of the application on the same maze.
	- Count the total number of choice points required by each version.
		- `LinkedQueue` should visit **247** choice points

Can you conclude anything from the differences in these results?

To test your program run the `main()` method in the *maze.py* file.
