import random
import numpy as np
import csv

csvPath = "sudoku-puzzles.csv"

def read_board_CSV(filePath):
    with open(filePath, mode ='r')as file:
        csvFile = csv.reader(file)
        rows = []
        for lines in csvFile:
            rows.append(lines)
    file.close()
 
# Transforms the board into a 2D list
    boards = []
    for row in rows:
        test = [int(x) for x in row[0]]
        test = np.reshape(test, (9,9))
        boards.append(test)
    return boards
    

def print_boards(board):
    for row in board:
        for cell in row:
            print(cell, end = " ")
        print(" ")
  
def cell_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return False

def is_valid(board, num, pos):
    # Check row
    if num in board[pos[0]]:
        return False
    # Check column
    if num in [board[i][pos[1]] for i in range(9)]:
        return False
    # Check 3x3 grid
    r = pos[0] // 3 * 3
    c = pos[1] // 3 * 3
    if num in [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]:
        return False
    return True

def solve_backtracking(board):
    empty = cell_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, empty):
            board[row][col] = num
            if solve_backtracking(board):
                return True
            else:
                board[row][col] = 0

def fill_box(board, row, col):
    num = random.randint(1, 9)
    for i in range(3):
        for j in range(3):
            while not is_valid(board, num, (row + i, col + j)):
                num = random.randint(1, 9)
            board[row + i][col + j] = num
    return board

def create_puzzle():
    k = random.randint(10, 40)
    board = [[0 for i in range(9)] for j in range(9)]
    # Fill the diagonal board with random numbers
    for i in range(0, 9, 3):
        board = fill_box(board, i, i)
    # Fill the rest of the board
    solve_backtracking(board)       
    # Remove k numbers from the board
    for i in range(k):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0
    return board
    
def main():
    print("Unsolved board:")
    board = create_puzzle()
    print_boards(board)
    solve_backtracking(board)
    print("\n")
    print("Solved board:")
    print_boards(board)
    
    
if __name__=="__main__":
    main()