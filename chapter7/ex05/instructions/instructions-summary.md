Write a program that converts __infix__ expressions to __postfix__ expressions. This program should use the `Token` and `Scanner` classes developed in the case study of this chapter.

A portion of the `convert()` method has been provided, but must be completed for the method to successfully convert the infix expression to postfix.

>Be sure to reuse your solution from *Programming Exercise 7.4* as your starter file for the *scanner.py* and *tokens.py* files.

In the `Token` class of the *tokens.py* file, complete the following:
1. Define the `getPrecedence()` method.
	- Returns an integer that represents the precedence level of an operator.
		- If the token contains the exponential operator (`EXPO`), return **3**
		- If the token contains the multiply (`MUL`) or the divide operator (`DIV`), return **2**
		- If the token contains the addition (`PLUS`) or the subtraction operator (`MINUS`), return **1**

In the `IFToPFConverter` class of the *converter.py* file, complete the following:
1. Complete the implementation of the `convert()` method.
	- This method returns a list of __tokens__  that represents the __postfix__ string (Assumes that the infix expression is syntactically correct).
	- When the stack is not empty and the precedence is greater or equal to the `currentToken` precedence:
		- Append the stack to `postfix`
	- If the stack `stack.isEmpty()` is empty and the exponential operator `Token.EXPO` is not the current token:
		- Push the `currentToken` to the stack
2. Complete the implementation of the `main()` method that performs the inputs and outputs.
	- The `main()` method receives an input string and creates a scanner with it. 
	- The scanner is then passed as an argument to the constructor of the converter object. 
	- The converter object’s `convert()` method is then run to convert the __infix__ expression using the algorithm described in this chapter.
	- The `main()` method then displays this string. 

>Note: You should assume for this project that the user always enters a syntactically correct __infix__ expression.

To test your program run the `main()` method in the *converter.py* file.

Your program's output should look like the following:
```
Enter an infix expression: 2 * 3 * 4
Postfix: 2 3 * 4 *
```