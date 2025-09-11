The `remove()` method performs two searches of a bag:
1. During the test of the method’s precondition (using the `in` operator)
2. To locate the position of the target item to actually remove it.

>Be sure to reuse your solution from *Programming Exercise 6.7* as your starter file for the *arraysortedbag.py*, *linkedbag.py*, *abstractbag.py*, *arrayset.py*, *linkedset.py* and *arraysortedset.py* files.

In the `ArrayBag` class of the *arraybag.py* file, complete the following:
1. Complete the implementation of the `__contains__` method to perform the customized search.
	- Eliminate the redundant search by tracking the position of the target item in an instance variable, `targetIndex`.
	- In the case of an array-based bag, this position would be __–1__ at startup and whenever a target item is not found.
	- If the `in` operator finds a target item, the position variable is set to that item’s index in the array; otherwise, it is reset to __–1__. 
	- After the `remove()` method checks its precondition, no search loop is necessary.
		- The method can just close the hole in the array using the position variable.

To test your program run the `test()` method in the *testset.py* file.
