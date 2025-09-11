Test for exponentiation to the expression tree developed in *Exercise 7* of this chapter to make sure `InteriorNode` handles the `^` operator and raises the values to the power of the provided parameters.

>Be sure to reuse your solution from *Programming Exercise 10.7* as your starter file for the *expressiontree.py* file.

In the *tokens.py* file, complete the following:
1. Add the `^` power operator to the available tokens, set it to **9** and name it as `EXPO`.
2. Modify the `_makeType` method to handle the `^` operator with the `EXPO` token.
3. Add a variable named **expo** to the `main()` method and print the exponentiation token to the tester program.

In the `InteriorNode` class of the *expressiontree.py* file, complete the following:
1. Modify the `computeValue()` method so that it handles the `EXPO` token.
	-  Raises the values to the power of the provided parameters of `value1` and `value2`.
	
To test your program run the `main()` method in the *expressiontree.py* file.

Your program's output should look like the following:
```
Expect ((4 * (2 + 3) ^ (2 + 3)): ((4 * (2 + 3)) ^ (2 + 3))
Expect ^ * 4 + 2 3 + 2 3       : ^ * 4 + 2 3 + 2 3
Expect 4 2 3 + * 2 3 + ^       : 4 2 3 + * 2 3 + ^
Expect 3200000                 : 3200000
```