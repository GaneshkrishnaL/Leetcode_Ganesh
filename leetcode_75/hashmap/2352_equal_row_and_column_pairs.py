from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        LeetCode 2352: Equal Row and Column Pairs

        Given an n x n matrix `grid`, count how many pairs (ri, cj) exist such that:
        - The entire row ri is equal to the entire column cj
        - Equality is element-wise and order-wise (same length and same value at each index)
        """

        # `rowmap` will store how many times each *row pattern* appears in the matrix.
        # Key  : a tuple representing a row (e.g., (3, 2, 1))
        # Value: count of how many times this exact row (same order) appears.
        #
        # defaultdict(int) gives a default value of 0 for unseen keys,
        # so we can safely do rowmap[key] += 1 without extra existence checks.
        rowmap = defaultdict(int)

        # This will store the total number of equal row–column pairs.
        count = 0

        # Step 1: Record all row patterns and their frequencies.
        # We convert each row (which is a list) into a tuple because:
        # - Lists are mutable and cannot be used as dictionary keys (unhashable).
        # - Tuples are immutable and hashable, so they are valid dictionary keys.
        # Using tuples preserves the exact order of elements in the row.
        for row in grid:
            # Example:
            # row = [3, 2, 1]  -> tuple(row) = (3, 2, 1)
            row_pattern = tuple(row)
            rowmap[row_pattern] += 1

        # The matrix is n x n, so the number of rows = number of columns = n.
        n = len(grid)

        # Step 2: For each column, build its pattern and check how many matching rows exist.
        #
        # Logic:
        # - For each column index `c` in [0, n):
        #     - Build the column as a tuple: (grid[0][c], grid[1][c], ..., grid[n-1][c])
        #     - Look up how many rows have exactly this pattern in `rowmap`
        #     - Add that frequency to `count`
        #
        # This works because:
        # - If a column pattern appears k times as a row pattern, then there are k pairs (ri, cj)
        #   where that column matches those rows.
        for c in range(n):
            # Build the column pattern for column `c` by collecting grid[r][c] for all rows r.
            # Using a generator inside tuple(...) keeps it compact and efficient.
            column_pattern = tuple(grid[r][c] for r in range(n))

            # If this column pattern exists in rowmap, then:
            # - rowmap[column_pattern] is the number of rows that look exactly like this column.
            # - Each of those rows forms a valid (row, column) pair with this column.
            if column_pattern in rowmap:
                count += rowmap[column_pattern]

        # Step 3: Return the total count of equal row–column pairs.
        return count
