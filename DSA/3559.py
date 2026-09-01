"""
Problem: Number of Ways to Assign Edge Weights II
LeetCode ID: 3559
Pattern: Trees / LCA / Binary Lifting
Difficulty: Hard

Time Complexity: O((n + q) log n)
Space Complexity: O(n log n)

Approach:
1. Build the tree using an adjacency list.
2. Run BFS from node 1 to compute:
      - depth of every node
      - immediate parent of every node
3. Precompute Binary Lifting table:
      parent[j][node]
   where parent[j][node] is the 2^j-th ancestor.
4. For each query (u, v):
      - Find LCA(u, v)
      - Compute path length:
            depth[u] + depth[v] - 2 * depth[lca]
5. Count valid edge-weight assignments:
      - Total assignments = 2^path_length
      - Exactly half have odd path sum
      - Answer = 2^(path_length - 1)
6. If path_length = 0:
      - No edges exist on the path
      - Sum is always 0 (even)
      - Answer = 0
7. Return all answers modulo 1e9 + 7.
"""

from typing import List
from collections import defaultdict, deque
import math


class Solution:
    def assignEdgeWeights(
        self,
        edges: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        LOG = max(1, math.ceil(math.log2(n))) + 1
        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]
        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([1])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[node] + 1
                    parent[0][neighbor] = node
                    queue.append(neighbor)
        for j in range(1, LOG):
            for node in order:
                parent[j][node] = parent[j - 1][parent[j - 1][node]]
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]
            return parent[0][u]
        result = []
        for u, v in queries:
            ancestor = lca(u, v)
            path_len = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )
            if path_len == 0:
                result.append(0)
            else:
                result.append(
                    pow(2, path_len - 1, MOD)
                )
        return result
    
    