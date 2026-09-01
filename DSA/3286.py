"""
Problem: Find a Safe Walk Through a Grid
LeetCode ID: 3286
Pattern: Graphs / 0-1 BFS
Difficulty: Medium

Time Complexity: O(m × n)
Space Complexity: O(m × n)

Approach:
1. Treat each cell as a graph node.
2. Moving into a safe cell (0) has cost 0,
   while moving into an unsafe cell (1) has cost 1.
3. Use 0-1 BFS to find the minimum health loss
   required to reach every cell:
      - Push cost-0 moves to the front.
      - Push cost-1 moves to the back.
4. If the minimum health loss to reach the
   destination is less than the initial health,
   the walk is possible.
"""

from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            d = dist[r][c]
            
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    nd = d + cost
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        
        return health - dist[m - 1][n - 1] > 0

        