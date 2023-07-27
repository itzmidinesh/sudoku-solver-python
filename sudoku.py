# Change the input in the below variable "puzzle" as per your needs.
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# Function to find the index of first occurrence of empty cell, i.e, 0
# returns None if no empty cell is found.
def findEmpty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==0:
                return [row, col]
    return None

# Function to check if the value(val) is present in the given row of puzzle.
def checkRow(puzzle,row,val):
    for i in range(9):
        if puzzle[row][i]==val:
            return False
    return True

# Function to check if the value(val) is present in the given column(col) of puzzle.
def checkColumn(puzzle,col,val):
    for i in range(9):
        if puzzle[i][col]==val:
            return False
    return True

# Function to check if the value(val) is present in the current  3*3 box of puzzle.
def checkBox(puzzle,row,col,val):
    # gets the index[r,c] of the first cell in current 3*3 box of puzzle.
    r= (row//3)*3
    c= (col//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[r+i][c+j]==val:
                return False
    return True

# Function to print the puzzle in a pretty format to the console.
def printPuzzle(puzzle):
    for x in puzzle:
        for y in x:
            print(y,end=" ")
        print()

# Function to solve the sudoku problem.
def sudoku(puzzle):
    find = findEmpty(puzzle)
    if not find:
        return True
    else:
        row, col = find
    for num in range(1,10):
        if checkRow(puzzle,row,num) and checkColumn(puzzle,col,num) and checkBox(puzzle,row,col,num):
            puzzle[row][col] = num
            if sudoku(puzzle):
                return True
            puzzle[row][col]=0
    return False

# Print statements to display the problem and solution in the console.
print("Problem:")
printPuzzle(puzzle)
if sudoku(puzzle):
    print("Solution:")
    printPuzzle(puzzle)
else:
    print()
    print("The problem is unsolvable, please try a different one.")
        
    
