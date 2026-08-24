"""
Problem: Maximum Depth of Binary Tree
LeetCode ID: 104
Pattern: Binary Tree / BFS / Level Order Traversal
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the tree is empty, its depth is 0.
2. Use a queue to perform level-order traversal.
3. Process all nodes belonging to the current level.
4. After processing one complete level, increase the depth.
5. Continue until all levels have been processed.
6. Return the total number of levels.
"""

from collections import deque
from typing import Optional


class Solution:
    def maxDepth(self,root: Optional["TreeNode"]) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth