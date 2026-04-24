"""
Problem: Zigzag Conversion
LeetCode ID: 6
Pattern: Strings / Simulation
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If numRows = 1 or numRows >= len(s), return s directly.
2. Create an array of strings for each row.
3. Traverse characters in s:
   - Append current character to current row.
   - Move downward or upward depending on direction.
4. Reverse direction when reaching:
   - top row
   - bottom row
5. Concatenate all rows to get final zigzag reading.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        direction = 1

        for ch in s:
            rows[cur_row] += ch

            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1

            cur_row += direction

        return "".join(rows)
    