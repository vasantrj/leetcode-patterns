"""
Problem: Rotate Image
LeetCode ID: 48
Pattern: Arrays / Matrix Manipulation
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(1)

Approach:
1. Rotate the matrix 90° clockwise in-place.
2. Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i]).
3. Step 2: Reverse each row.
4. This results in the desired rotation without extra space.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

