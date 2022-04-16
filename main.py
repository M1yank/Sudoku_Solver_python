from distutils.log import error
from pprint import pprint
from solve_sudoku import solve

# Input the sudoku 
grid = []
for i in range(9):
    row=list(input('Enter row {} : '.format(i+1)))
    grid.append(row)

sudoku = [[int(num) for num in item] for item in grid]     #converts above grid(list in list) to int form from string

print("\nYour Sudoku : \n")
pprint(sudoku)
print('\n')

if solve(sudoku):
    print("This Sudoku has valid solution : ")
    pprint(sudoku)

else:
    error("This suduko is UNSOLVABLE, kindly check input and try to run code again!!!")
