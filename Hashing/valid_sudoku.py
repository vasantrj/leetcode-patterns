"""
Problem: Valid Sudoku
LeetCode ID: 36
Pattern: Hashing / Set
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Use three sets:
   - rows → track numbers in each row
   - cols → track numbers in each column
   - boxes → track numbers in each 3x3 sub-box
2. Traverse each cell in the 9x9 board:
   - Skip '.' (empty cells)
   - Check if number already exists in row, column, or box
   - If yes → return False
3. Otherwise, add number to corresponding sets
4. If no conflicts found → return True
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_index]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True