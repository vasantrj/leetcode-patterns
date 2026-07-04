"""
Problem: Minimum Score of a Path Between Two Cities
LeetCode ID: 2492
Pattern: Graphs / DFS
Difficulty: Medium

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Approach:
1. Build an undirected graph using an adjacency list.
2. Start a DFS from city 1 to visit every city in its
   connected component.
3. While traversing, keep track of the minimum road
   distance encountered.
4. Since every city in the connected component can be
   visited multiple times, the answer is simply the
   smallest edge in the component containing city 1.
"""

from collections import defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        visited = [False] * (n + 1)
        ans = float('inf')
        stack = [1]
        visited[1] = True
        while stack:
            node = stack.pop()
            for neighbor, dist in graph[node]:
                ans = min(ans, dist)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        return ans