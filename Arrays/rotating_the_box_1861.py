"""
Problem: Rotating the Box
LeetCode ID: 1861
Pattern: Arrays / Matrix Simulation
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Simulate gravity for each row:
   - Stones '#' fall to the right until blocked by:
     - obstacle '*'
     - another stone
2. Use a pointer `empty` to track the rightmost available position.
3. After gravity simulation:
   - Rotate the matrix 90° clockwise.
4. Return rotated matrix.
"""

from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for r in range(rows):
            empty = cols - 1

            for c in range(cols - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    empty = c - 1

                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1

        rotated = [[None] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = boxGrid[r][c]

        return rotated
    