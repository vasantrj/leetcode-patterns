"""
Problem: Detect Cycles in 2D Grid
LeetCode ID: 1559
Pattern: Graphs / DFS / Matrix Traversal
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Traverse each cell in the grid.
2. Start DFS from every unvisited cell.
3. Move only to adjacent cells (up, down, left, right)
   having the same character.
4. While exploring:
   - Track parent cell to avoid going back immediately.
   - If we reach an already visited same-character cell
     that is not the parent, a cycle exists.
5. Return True if any cycle is found, else False.
"""

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, pr: int, pc: int, char: str) -> bool:
            visited[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, char):
                            return True
                    elif nr != pr or nc != pc:
                        return True

            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True

        return False
    
    