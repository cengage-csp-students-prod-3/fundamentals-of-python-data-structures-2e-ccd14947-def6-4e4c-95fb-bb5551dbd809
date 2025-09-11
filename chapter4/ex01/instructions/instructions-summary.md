In the `Array` class of the *arrays.py* file complete the following:
1. Modify the `__init__` method to add an instance variable ```logicalSize```.
	- This variable is initially **0** and will track the number of items currently available to users of the array. 
2. Define the ``` size() ``` method. 
	- This method should return the array’s logical size.
	- The method ```__len__ ```should still return the array’s capacity or physical size.
	
To test your program run the `main()` method in the *arrays.py* file.
	
Your program's output should look like the following:
```
Physical size: 10
Logical size: 0
Items: [None, None, None, None, None, None, None, None, None, None]
```	
