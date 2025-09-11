Add the `^` operator to the language of expressions processed by the expression evaluator of the case study.
Changes should be made in the _tokens.py_ and _model.py_ files. This operator has the same semantics as Python’s `exponentiation` operator. Thus, the expression `2 2 3 ^ ^` evaluates to __256__.

>Be sure to reuse your solution from *Programming Exercise 7.3* as your starter file for the *scanner.py* file.

In the `Token` class of the *tokens.py* file, complete the following:
1. Add the exponential operator (`^`), to the language of expressions processed by the expression evaluator.
	- Add an instance variable as **EXPO** and set the exponent operator to **9**
	- In the `makeType()` method add the exponential operator
	- In the `main()` method set `expo` equal to the exponential operator token
		- Add `expo` to the print statement

In the `PFEvaluator` class of the *model.py* file, complete the following:
1. Modify the `computeValue()` method.
	- Add the ability to handle the `EXPO` exponential operator in the evaluation

To test your program run the `run()` method in the *evaluatorapp.py* file.

Your program's output should look like the following:
```
Enter a postfix expression: 2 2 3 ^ ^
2 2 3 ^ ^ 
256
```