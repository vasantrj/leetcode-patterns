"""
Problem: Max Area of Island
LeetCode ID: 695
Pattern: Graphs / DFS / Matrix Traversal
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n) worst case recursion stack

Approach:
1. Traverse every cell in the grid.
2. If a cell contains 1 (land), start DFS.
3. DFS explores connected land cells in 4 directions:
   up, down, left, right.
4. Count number of cells in the current island.
5. Track maximum area among all islands.
6. Mark visited land as 0 to avoid revisiting.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area