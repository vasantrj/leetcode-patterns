"""
Problem: Binary Tree Inorder Traversal
LeetCode ID: 94
Pattern: Binary Tree, Depth-First Search, Recursion
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Recursively traverse the left subtree.
2. Add the current node's value to the result.
3. Recursively traverse the right subtree.
4. Continue until all nodes are visited.

Key Insight:
Inorder traversal follows the order:
Left → Root → Right

For a Binary Search Tree, this traversal produces values in sorted order.
"""

from typing import List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result