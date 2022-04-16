def guess(sudoku, x, i, j):
    #checks if x is valid according to current board
    #return true if valid
    
    #row check
    row = sudoku[i]
    if x in row:
        return False
    
    #column check
    col=[]
    for m in range(9):
        col.append(sudoku[m][j])
    if x in col:
        return False
    
    #3x3 block check
    row_start = (i // 3 ) * 3
    col_start = (j // 3 ) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if sudoku[r][c] == x:
                return False

    #passed all checks
    return True