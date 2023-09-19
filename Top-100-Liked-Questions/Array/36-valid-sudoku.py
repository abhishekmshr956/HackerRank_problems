""" https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
def isValidVector(A):
    count = set()
    for a in A:
        if a != '.':
            i = int(a)
            if i in count:
                return False
            count.add(i)
    return True

def isValidSudoku(board):

    # check if all rows are valid
    for row in board:
        if not isValidVector(row):
            return False
        
    # check if all columns are valid
    for i in range(len(board)):
        column = []
        for j in range(len(board)):
            column.append(board[j][i])
        if not isValidVector(column):
            return False
        
    # check if all 3*3 blocks are valid
    for o in range(3):
        for i in range(3):
            miniboard = []
            for j in range(3):
                for k in range(3):
                    miniboard.append(board[j + 3*o][k+3*i])
            if not isValidVector(miniboard):
                return False

    return True 

if __name__ == '__main__':
    A = ["5","3",".",".","7","5",".",".","."]
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))