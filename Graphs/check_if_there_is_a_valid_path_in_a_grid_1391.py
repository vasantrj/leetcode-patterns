"""
Problem: Check if There is a Valid Path in a Grid
LeetCode ID: 1391
Pattern: Graphs / BFS / Matrix Traversal
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Each street type connects in specific directions.
2. Start BFS from (0,0).
3. Move only if:
   - Current cell has a road toward neighbor.
   - Neighbor cell has a matching road back.
4. Visit each cell once.
5. If bottom-right cell is reached, return True.
"""

from collections import deque

class Solution(object):
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
    
