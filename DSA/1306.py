"""
Problem: Jump Game III
LeetCode ID: 1306
Pattern: Graphs / BFS / DFS
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Treat each index as a graph node.
2. From index i, possible moves:
   - i + arr[i]
   - i - arr[i]
3. Use BFS/DFS to explore reachable indices.
4. Track visited indices to avoid infinite loops.
5. If any reachable index contains value 0:
   return True.
6. Otherwise return False.
"""

from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True

        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

        return False
    