Define a function named insert that ``` inserts ``` an item into a singly linked structure at a given position. 
The function expects three arguments: the item, the position, and the linked structure. (The latter may be empty.) 
The function returns the modified linked structure.

If the position is greater than or equal to the structure’s length, the function inserts the item at its end.


An example call of the function, 
where ``` head ``` is a variable that either is an empty link or refers to the first node of a structure, is


```head = insert(1, data, head).``` 
