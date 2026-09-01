"""
Problem: Create Binary Tree From Descriptions
LeetCode ID: 2196
Pattern: Trees / Hash Map
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a hashmap to create/reuse TreeNode objects.
2. For each description:
   - parent, child, isLeft
   - Connect child to parent.
3. Track all child nodes in a set.
4. The root is the node that never appears as a child.
5. Return the root node.
"""

from typing import List, Optional


class Solution:
    def createBinaryTree(
        self,
        descriptions: List[List[int]]
    ) -> Optional[TreeNode]:

        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for value in nodes:
            if value not in children:
                return nodes[value]

        return None