def find_empty_space(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r,c
    
    return None, None