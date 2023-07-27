puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def findEmpty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==0:
                return [row, col]
    return None

def checkRow(puzzle,row,val):
    for i in range(9):
        if puzzle[row][i]==val:
            return False
    return True
def checkColumn(puzzle,col,val):
    for i in range(9):
        if puzzle[i][col]==val:
            return False
    return True
def checkBox(puzzle,row,col,val):
    r= (row//3)*3
    c= (col//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[r+i][c+j]==val:
                return False
    return True

def printPuzzle(puzzle):
    for x in puzzle:
        for y in x:
            print(y,end=" ")
        print()

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
print("Problem: ")
printPuzzle(puzzle)
if sudoku(puzzle):
    print("Solution: ")
    printPuzzle(puzzle)
else:
    print("The problem is unsolvable, please try a different one.")


        
    
