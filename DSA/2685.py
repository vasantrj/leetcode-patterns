"""
Problem: Count the Number of Complete Components
LeetCode ID: 2685
Pattern: Graphs / Union Find
Difficulty: Medium

Time Complexity: O((n + m) · α(n))
Space Complexity: O(n)

where:
    n = number of nodes
    m = number of edges
    α(n) = inverse Ackermann function (nearly constant)

Approach:
1. Use Union-Find (Disjoint Set Union) to group all
   connected nodes into components.
2. Count:
      - Number of nodes in each component.
      - Number of edges in each component.
3. For every connected component:
      - A complete graph with k nodes must contain
        k × (k - 1) / 2 edges.
4. Count every component whose edge count matches
   the expected number of edges.
"""

from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        
        for u, v in edges:
            union(u, v)
        
        node_count = [0] * n
        edge_count = [0] * n
        
        for i in range(n):
            node_count[find(i)] += 1
        
        for u, v in edges:
            root = find(u)
            edge_count[root] += 1
        
        result = 0
        for i in range(n):
            if find(i) == i:
                nodes = node_count[i]
                edges_in_comp = edge_count[i]
                if edges_in_comp == nodes * (nodes - 1) // 2:
                    result += 1
        
        return result