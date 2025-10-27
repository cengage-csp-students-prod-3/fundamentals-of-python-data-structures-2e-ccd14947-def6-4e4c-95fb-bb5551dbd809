"""
File: maze.py
Project 7.9

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a stack-based backtracking algorithm.
"""

from grid import Grid
from arraystack import ArrayStack

def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    success = getOut(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        print(maze)
# playing with writing to a file
        with open("mazeFinal.txt", "w", encoding="utf-8") as f:
            f.writelines("heres my file!!")
    else:
        print("No path out of this maze")
    
# def getMazeFromFile(file_path):
#     """Reads the maze from a text file and returns a grid that
#     represents it."""
#     try:
#         with open(file_path, 'r') as file:
#             maze = [list(line.strip()) for line in file]
#         return maze
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return None

def getMazeFromFile():
    """Reads the maze from a text file and returns a grid that
    represents it."""
    name = input("Enter a file name for the maze: ")
    fileObj = open(name)
    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    columns = firstLine[1]
    maze = Grid(rows, columns, "*")
    for row in range(rows):
        line = fileObj.readline().strip()
        column = 0
        for ch in line:
            maze[row][column] = ch
            column += 1

    return maze

    

def findStartPos(grid):
    """Returns the position of the start symbol in the grid."""
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 'P':  # Look for the starting position
                return (row_index, col_index)
    return None  # Return None if no starting position is found

def getOut(row, column, maze):
    """(row,column) is the position of the start symbol in the maze.
    Returns True if the maze can be solved or False otherwise."""
    # States are tuples of coordinates of cells in the grid.
    stack = ArrayStack()
    
    #Starts with the intial values of start position, these are the first
    #values addes to the stack.
    #
    stack.push((row, column))
    while not stack.isEmpty():
        (row, column) = stack.pop()
        if  maze[row][column] == 'T': 
            return True
        elif maze[row][column] != '.':
            # Cell has not been visited, so mark it and push adjacent unvisited
            # positions onto the stack
            maze[row][column] = '.'
            # Try NORTH
            if row != 0 and not maze[row - 1][column] in ('*', '.'):
                stack.push((row - 1, column))             
            # Try SOUTH
            if row + 1 != maze.getHeight() and not maze[row + 1][column] in ('*', '.'):         
                stack.push((row + 1, column))             
            # Try EAST
            if column + 1 != maze.getWidth() and not maze[row][column + 1] in ('*', '.'):     
                #This is possible cell to explore, at it to the stack    
                stack.push((row, column + 1))             
            # Try WEST
            if column != 0 and not maze[row][column - 1] in ('*', '.'):         
                stack.push((row, column - 1))

    return False

if __name__ == "__main__": main()
