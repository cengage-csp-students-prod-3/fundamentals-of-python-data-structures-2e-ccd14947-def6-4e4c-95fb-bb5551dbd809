Define a recursive, Boolean function named `equals` for two Lisp-like lists. 

The `equals()` method should check for the following:
1. Two lists are equal if they are both empty
2. Two lists are not equal if one is empty
3. Two list are equal if lengths of the lists are the same, their first items are equal and the rest of their items are equal.

Here is an example of its use: 

```
>>> lyst = buildRange(1, 5)
>>> lyst
(1 2 3 4 5)
>>> equals(lyst, buildrange(1, 5))
True
>>> equals(lyst, buildrange(1, 4))
False
```

