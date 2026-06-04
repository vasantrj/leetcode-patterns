"""
Problem: Decode the Slanted Ciphertext
LeetCode ID: 2075
Pattern: Strings / Matrix Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. The encoded text represents a matrix with:
   - given number of rows
   - columns = len(encodedText) // rows
2. The original message was written diagonally:
   - start from each column in the first row
   - move diagonally down-right
3. Reconstruct the decoded string by:
   - traversing each diagonal starting from top row
4. Finally, remove trailing spaces from the decoded message.
"""

from typing import List

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        cols = len(encodedText) // rows
        result = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                result.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return ''.join(result).rstrip()