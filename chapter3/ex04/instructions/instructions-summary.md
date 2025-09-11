An alternative strategy for the `expo()` function uses the following recursive
definition:

<blockquote>
         expo(base, exponent) <br>
         = 1, when exponent = 0 <br>
         = base * expo(base, exponent - 1), when exponent is odd <br>
         = (expo(base, exponent / 2))<sup>2</sup>, when exponent is even <br>
</blockquote>

Define a recursive function `expo()` that uses this strategy.

To test your program run the `main()` method in the *expo.py* file.

Your program's output should look like the following:
```
0 1
1 2
2 4
3 8
4 16
```
