"""
LeetCode Problem 36: Valid Sudoku
Difficulty: Medium

Problem Description:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Approach: Hash Set Tracking
- Use three separate hash tables (dictionaries) to track:
  1. Numbers seen in each row
  2. Numbers seen in each column
  3. Numbers seen in each 3x3 sub-box
- For each cell, check if the number already exists in the corresponding row, column, or sub-box
- If it does, the board is invalid
- Otherwise, add the number to all three tracking structures

Time Complexity: O(1) - Since board size is fixed at 9x9, we iterate through exactly 81 cells
Space Complexity: O(1) - Maximum space used is for storing 9 sets each for rows, columns, and boxes

Runtime: 0ms (Beats 100.00%)
Memory: 17.18 MB (Beats 100.00%)
"""

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates a Sudoku board by checking rows, columns, and 3x3 sub-boxes.
        
        Args:
            board: A 9x9 2D list representing the Sudoku board
                   '.' represents an empty cell
                   '1'-'9' represent filled cells
        
        Returns:
            bool: True if the board is valid, False otherwise
        """
        
        # Initialize hash tables to track seen numbers
        # defaultdict(set) creates an empty set for each key automatically
        row = defaultdict(set)      # row[i] = set of numbers in row i
        col = defaultdict(set)      # col[j] = set of numbers in column j
        squares = defaultdict(set)  # squares[(i//3, j//3)] = set of numbers in that 3x3 box
        
        # Iterate through every cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                
                # Skip empty cells (marked with '.')
                if board[i][j] == ".":
                    continue
                
                # Check if current number already exists in:
                # - Current row (row[i])
                # - Current column (col[j])
                # - Current 3x3 sub-box (squares[(i//3)*3 + (j//3)])
                # The sub-box key is calculated by dividing row and column by 3
                # to get which of the 9 boxes we're in (0-8)
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[((i//3)*3)+(j//3)]:
                    # Duplicate found - board is invalid
                    return False
                
                # Add the current number to all three tracking structures
                row[i].add(board[i][j])                      # Add to current row's set
                col[j].add(board[i][j])                      # Add to current column's set
                squares[((i//3)*3)+(j//3)].add(board[i][j])  # Add to current 3x3 box's set
        
        # If we've checked all cells without finding duplicates, board is valid
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Valid Sudoku board
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Test 1 - Valid board: {solution.isValidSudoku(board1)}")  # Expected: True
    
    # Test case 2: Invalid Sudoku board (duplicate 8 in first column)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Test 2 - Invalid board: {solution.isValidSudoku(board2)}")  # Expected: False
