"""
Problem: Find the Safest Path in a Grid
LeetCode ID: 2812
Pattern: Graphs / Multi-Source BFS + Dijkstra
Difficulty: Hard

Time Complexity: O(n² log n)
Space Complexity: O(n²)

Approach:
1. Perform a multi-source BFS starting from all thief cells
   to compute the minimum distance from every cell to its
   nearest thief.
2. Use a max-heap (modified Dijkstra) to find a path from
   (0, 0) to (n-1, n-1) that maximizes the minimum distance
   to any thief along the path.
3. For each move, the path's safeness is:
      min(current_safeness, distance_to_nearest_thief)
4. Always explore the path with the highest current safeness
   first.
5. The first time the destination is reached, its safeness
   factor is the maximum possible.
"""

from collections import deque
from typing import List
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == INF:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]
        max_heap = [(-dist[0][0], 0, 0)]
        while max_heap:
            neg_safe, x, y = heapq.heappop(max_heap)
            cur_safe = -neg_safe
            
            if cur_safe < safeness[x][y]:
                continue
            
            if x == n - 1 and y == n - 1:
                return cur_safe
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_safe = min(cur_safe, dist[nx][ny])
                    if new_safe > safeness[nx][ny]:
                        safeness[nx][ny] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nx, ny))
        
        return safeness[n-1][n-1]


        