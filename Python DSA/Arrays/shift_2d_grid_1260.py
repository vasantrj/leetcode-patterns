"""
Problem: Shift 2D Grid
LeetCode ID: 1260
Pattern: Arrays / Matrix
Difficulty: Easy

Time Complexity: O(m × n)
Space Complexity: O(m × n)

Approach:
1. Treat the 2D grid as a single flattened array.
2. For each element, compute its new position after shifting by k:
      new_index = (current_index + k) % (m × n)
3. Place the element into its new position in the flattened array.
4. Convert the flattened array back into a 2D grid.
"""

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [0] * (m * n)
        
        for i in range(m):
            for j in range(n):
                idx = (i * n + j + k) % (m * n)
                flat[idx] = grid[i][j]
        
        return [flat[i * n:(i + 1) * n] for i in range(m)]