<!-- practice -->

Write a program that solves the maze problem discussed earlier in this chapter.
You should use the `Grid` class developed in _Chapter 4, Exercise 7_ in this problem.

1.  Take a text file as an input for the maze's description.
2.  Display the maze based off the description.
3.  Program attempts to find solution.
4.  Displays the result.
5.  Displays the maze again.

In the _maze.py_ file, complete the following:

1. Complete the implementation of the `getMazeFromFile()` method.
   - Reads the maze from a text file
   - Returns a grid that represents it.
2. Complete the implementation of the `findStartPos()` method.
   - Returns the position of the start symbol in the grid.
3. Complete the implementation of the `getOut()` method.
   - (row,column) is the position of the start symbol in the maze.
   - States are tuples of coordinates of cells in the grid.
   - If a cell has not been visited, mark it and push adjacent unvisited positions onto the stack.
   - Try NORTH, SOUTH, EAST and WEST coordinates
   - Returns True if the maze can be solved or False otherwise.

To test your program run the `main()` method in the _maze.py_ file.

Your program's output should look like the following:

```
Enter a file name for the maze: maze.txt
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * *                                                             * * * * * * * *   * * * *
* * * * * * *   * * * * * * * * * * * * * *   * * * * * * * * * * * * *   * * * * * * * *   * * * *
* * * * * * *   * * * * * * * * * * * * * *   * * *                   *   * * *             * * * *
P               * * * * * * * * * * * * * *   * *     * * * * * *     *   * * *   * * * *   * * * *
* * * * * * *   * * *                   * *   *     * * * * * * *                 * * * *   * * * *
* * * * * * *   * * *   * * * * * * *   * *   *     * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * *   * * *   * * * * * * *   * *         * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * *   * * *   * * * * * * *   * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * *   * * *   * *                                             * * * * * * * * *   * * * *
* * *           * * *   * *   * * * *   * * * *   * * * * * * * * * * * * * * * * * * * *   * * * *
* * *   * * * * * * * * * *   * * * *   * * * *                               * * * * * *   * * * *
* * *   * * * * * * * * * *   * * * *   * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * *   * * * * * * * * * *   * * * *   * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * *                         * * * *   * * * * * * * * * * * *   * * * * * * * * * * * *   * * * *
* * * * * * * *   * * * * * * * * * *   * * * * * * * * * * * *   * * * * * * * * * * * *   * * * *
* * * * * * * *   * * * * * * * * * *   * * * * * * * * * * * *             * * * * * * *   * * * *
* * * * * * * *             * * * * *   * * * * * * * * * * * *   * * * *   * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * *                             * * * *   * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *                         T
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Maze solved:
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * *                                                             * * * * * * * *   * * * *
* * * * * * *   * * * * * * * * * * * * * *   * * * * * * * * * * * * *   * * * * * * * *   * * * *
* * * * * * *   * * * * * * * * * * * * * *   * * *                   *   * * *             * * * *
. . . . . . . . * * * * * * * * * * * * * *   * *     * * * * * *     *   * * *   * * * *   * * * *
* * * * * * * . * * *                   * *   *     * * * * * * *                 * * * *   * * * *
* * * * * * * . * * *   * * * * * * *   * *   *     * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * * . * * *   * * * * * * *   * *         * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * * . * * *   * * * * * * *   * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * * * * * * . * * *   * * . . . . . . . . . . . . . . . . . . . . . . * * * * * * * * *   * * * *
* * * . . . . . * * *   * * . * * * * . * * * * . * * * * * * * * * * * * * * * * * * * *   * * * *
* * * . * * * * * * * * * * . * * * * . * * * * . . . . . . . . . . . . . . . * * * * * *   * * * *
* * * . * * * * * * * * * * . * * * * . * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * * . * * * * * * * * * * . * * * * . * * * * * * * * * * * * * * * * * * * * * * * * *   * * * *
* * * . . . . . . . . . . . . * * * * . * * * * * * * * * * * *   * * * * * * * * * * * *   * * * *
* * * * * * * *   * * * * * * * * * * . * * * * * * * * * * * *   * * * * * * * * * * * *   * * * *
* * * * * * * *   * * * * * * * * * * . * * * * * * * * * * * * . . . . . . * * * * * * *   * * * *
* * * * * * * *             * * * * * . * * * * * * * * * * * * . * * * * . * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * * . . . . . . . . . . . . . . * * * * . * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * . * * * * * * *   * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * . * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * . . . . . . . . . . . . T
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

> The test above used the _maze.txt_ file to test.
