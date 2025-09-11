<!-- manual -->

Jill tells Jack that he should now remove the current implementation of the`__iter__`
method from the `Array` class, if it’s really behaving like a list.

> Be sure to reuse your solution from _Programming Exercise 4.5_ as your starter file for the _arrays.py_ file.

To test your program run the `main()` method below in the _arrays.py_ file:

```
def main():
    """Test code for modified Array class."""
    a = Array(10)
    for item in range(4):
        a.insert(0, item)
    print(a)

if __name__ == "__main__":
    main()
```

Explain why this is a good suggestion. Also explain how the` __str__` method should be modified at this point in the docstring.
