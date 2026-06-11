"""
Problem: Number of Ways to Assign Edge Weights I
LeetCode ID: 3558
Pattern: Trees / BFS / Combinatorics
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build the tree using an adjacency list.
2. Run BFS from node 1 to compute the depth of every node.
3. Find the maximum depth in the tree.
4. The path from the root to a deepest node contains
   exactly max_depth edges.
5. Each edge can be assigned weight 1 or 2:
      Total assignments = 2^max_depth
6. By parity symmetry:
      Half of the assignments produce an odd sum,
      half produce an even sum.
7. Therefore:
      Answer = 2^(max_depth - 1)
8. Return the answer modulo 1e9 + 7.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [-1] * (n + 1)
        depth[1] = 0
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if depth[neighbor] == -1:
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)

        max_depth = max(depth[1:])
        return pow(2, max_depth - 1, MOD)