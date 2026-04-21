"""
Problem: Number of Islands
LeetCode ID: 200
Pattern: Graphs / DFS / Matrix Traversal
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n) worst case recursion stack

Approach:
1. Traverse every cell in the grid.
2. If a cell contains '1' (land), it is a new island.
3. Run DFS to mark all connected land cells (up, down, left, right) as visited.
4. Increment island count for each new DFS start.
5. Return total islands found.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return

            grid[r][c] = '0'  # mark visited

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands