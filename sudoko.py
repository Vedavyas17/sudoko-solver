"""
Question:
A sudoku solution must satisfy all of the following rules:

1)Each of the digits 1-9 must occur exactly once in each row.
2)Each of the digits 1-9 must occur exactly once in each column.
3)Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '0' character indicates empty cells.

 Using Backtracking Approach:

 Sudoku can be solved by one by one assigning numbers to empty cells.
 Before assigning a number, check whether it is safe to assign.
 Check that the same number is not present in the current row, current column and current 3X3 subgrid.
 After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not.
 If the assignment doesn’t lead to a solution,then try the next number for the current empty cell.
 And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.
"""
import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#  sudoko solver using backtracking algorithm:
# 18008969999
def conditions(row, col, num):
    global grid
    # if respective rowor column has same number
    for a in range(0,9):
        if grid[row][a] == num or grid[a][col] == num:
            return False
    # finding the starting position of the grid
    startingRow = (row // 3) * 3 # this will define the curent row position
    startingCol = (col // 3) * 3 # this will define the curent column position
    for i in range(0,3):
        for j in range(0,3):
            if grid[startingRow + i][startingCol + j] == num:
                return False
    return True

def sudoko():
    global grid
    for row in range(0, 9):
        for col in range(0, 9):
            #check if the number is 0. if 0 then call the function conditions
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if conditions(row, col, num):
                        grid[row][col] = num
                        # again try solving for the remaining positions
                        sudoko()
                        grid[row][col] = 0
                return

    print(np.matrix(grid))
    input('Other possibilities :')


sudoko()
