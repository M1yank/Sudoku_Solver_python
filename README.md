# Sudoku Solver python
# 👩‍💻Description:
A python script to solve sudoku using backtracking.

Basically this script finds a empty space (0) in the sudoku and checks whether it is possible solution. If the guess is valid, we find next empty space and loop continues until we find no empty spaces. But lets say that our 3rd guess is not valid than it will than it will backtrack and iterate next guess and continue the loop.
More information is stated in comments in the code of sudoku solver.

# 📝Steps to run:
1. Make sure that all 4 files are in one folder.
2. Run main.py
3. Input the sudoku in row format without any spaces and append 0 where sudoku is empty.

## Example : Let's take a sudoku : 

   ![sudoku_example](https://user-images.githubusercontent.com/95163425/163683453-14edd439-89e7-4b7b-8209-9bf08bf719e0.jpg)

So the input format will be : 

Row 1: 050037090

Row 2: 000002000

Row 3: 800000500

Row 4: 000600000

Row 5: 004000001

Row 6: 080095070

Row 7: 100063007

Row 8: 030200000

Row 9: 000800060

## If the sudoku is valid, solution will be printed. 
