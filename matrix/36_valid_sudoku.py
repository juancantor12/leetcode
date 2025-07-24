"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution(object):
    """
    This solution works by creating containers for all subsets that should have unique items
    as the matrix is traversed, each element will be checked agains its corresponding row, col and square
    if the value is not in any of those, it is added to each and the process continue
    if at any point a value is already on any of the subsets, return false since is no longer valid.
    """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[] }  # Subset for the rows
        columns = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[] }  # Subset for the columns
        squares = {
            (0,0):[], (0,1):[], (0,2):[], 
            (1,0):[], (1,1):[], (1,2):[], 
            (2,0):[], (2,1):[], (2,2):[]
        }  # Subset for the squares, each squeare key is a tuble of its coordinates on a 3 by 3 square grid

        for i in range(9):  # iterate rows
            for j in range(9):  # iterate columns
                cell = board[i][j]  # get the current cell value
                if cell != '.':  # Only proceed if the cell has a value
                    # If the value is on any of the corresponding row, column or square, is not a valid setting
                    # To address the square key, modding the current row and column by 3 gives the appropiate coordinate
                    if cell in rows[i] or cell in columns[j] or cell in squares[i//3, j//3]:
                        return False  #  and we return false
                    rows[i].append(cell)  # Otherwise, add the value to the corresponding col
                    columns[j].append(cell)  # row
                    squares[i//3, j//3].append(cell)  # and square ground
        # If the algorith didn't stopped early, this means the sudoku is valid (even if not solvable)
        return True
