The exponential operator has a higher precedence than either `*` or `/`. Also, this operator is __right associative__, which means that consecutive applications of this operator are evaluated from right to left rather than from left to right. 

>Be sure to reuse your solution from *Programming Exercise 7.5* as your starter file for the *scanner.py*, *tokens.py* and *converter.py* files.

Thus, the value of the expression `2 ^ 2 ^ 3` is equivalent to `2 ^ (2 ^ 3)` or __256__, not `(2 ^ 2) ^ 3` or __64__.
You must modify the algorithm from __infix__ to __postfix__, a conversion to place the operands as well as the operators in the appropriate positions in the __postfix__ string.


In the `Token` class of the *tokens.py* file, complete the following:
1. Add the left parenthesis operator (`(`), to the expression language processed by the __infix__ to __postfix__ converter.
	- Add an instance variable as **LPAR** and set the right parenthesis operator to **10**
	- In the `makeType()` method add the left parenthesis operator
2. Add the right parenthesis operator (`)`), to the expression language processed by the __infix__ to __postfix__ converter.
	- Add an instance variable as **RPAR** and set the right parenthesis operator to **11**
	- In the `makeType()` method add the right parenthesis operator

In the `IFToPFConverter` class of the *converter.py* file, complete the following:
1. Modify the `convert()` method to include the left and right parenthesis for proper conversion of operands and operators in parentheses to the __postfix__ string.
	- If the current token is `LPAR`
		- Push the `currentToken` to the stack
	- If the current token is `RPAR`
		- Remove the item at the top of stack and set it as **topOperator**
			- While **topOperator** is not equal to `LPAR`
				- Append the **topOperator** to `postfix`
				- Remove the item at the top of the stack

To test your program run the `main()` method in the *converter.py* file.

Your program's output should look like the following:
```
Enter an infix expression: 2 ^ 2 ^ 3
Postfix: 2 2 3 ^ ^ 
Enter an infix expression: 2 ^ (2 ^ 3)
Postfix: 2 2 3 ^ ^ 
```
> The test above is using the **2 ^ 2 ^ 3** and then with parentheses **2 ^ (2 ^ 3)** as the infix expressions.