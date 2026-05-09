"""
Problem: Cyclically Rotating a Grid
LeetCode ID: 914
Pattern: Arrays / Matrix Simulation
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Process the grid layer by layer.
2. Extract each layer into a linear list in clockwise order.
3. Rotate the layer by k positions.
4. Place rotated values back into the grid.
5. Repeat for all layers.
6. Return final rotated grid.
"""

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        layers = min(rows, cols) // 2
        for layer in range(layers):
            elems = []
            top = layer
            bottom = rows - layer - 1
            left = layer
            right = cols - layer - 1

            for c in range(left, right + 1):
                elems.append(grid[top][c])

            for r in range(top + 1, bottom):
                elems.append(grid[r][right])

            for c in range(right, left - 1, -1):
                elems.append(grid[bottom][c])

            for r in range(bottom - 1, top, -1):
                elems.append(grid[r][left])

            rot = k % len(elems)
            rotated = elems[rot:] + elems[:rot]
            idx = 0

            for c in range(left, right + 1):
                grid[top][c] = rotated[idx]
                idx += 1

            for r in range(top + 1, bottom):
                grid[r][right] = rotated[idx]
                idx += 1

            for c in range(right, left - 1, -1):
                grid[bottom][c] = rotated[idx]
                idx += 1

            for r in range(bottom - 1, top, -1):
                grid[r][left] = rotated[idx]
                idx += 1

        return grid