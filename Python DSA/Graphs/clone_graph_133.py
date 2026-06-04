"""
Problem: Clone Graph
LeetCode ID: 133
Pattern: Graphs / DFS / Hash Map
Difficulty: Medium
Time Complexity: O(V + E)
Space Complexity: O(V)

Approach:
1. If input node is None, return None.
2. Use DFS to traverse the graph.
3. Maintain a hashmap:
   original node -> cloned node
4. For each node:
   - Create clone if not already created.
   - Recursively clone all neighbors.
5. Return cloned starting node.
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in clones:
                return clones[curr]

            copy = Node(curr.val)
            clones[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
    
