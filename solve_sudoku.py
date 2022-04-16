from find_empty import find_empty_space
from valid_guess import guess

def solve(sudoku):
    #solve using backtracking
    #1. Find empty cell on sudoku
    i, j = find_empty_space(sudoku) 

    #no empty space
    if i is None:
        return True

    #found empty space and guess
    for x in range(1,10):
        if guess(sudoku, x, i, j):
            sudoku[i][j] = x

            #solve this sudoku with this guess
            if solve(sudoku):
                return True

        #backtrack if not valid guess
        sudoku[i][j] = 0

    #if not solvable, 
    return False