"""
Problem: Balanced Binary Tree
LeetCode ID: 110
Pattern: Binary Tree, DFS, Recursion
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Recursively calculate the height of each subtree.
2. If a subtree is already unbalanced, return -1 immediately.
3. Check whether the height difference between the left and right
   subtrees is greater than 1.
4. Return the subtree height if balanced, otherwise return -1.
5. The tree is balanced if the final height is not -1.

"""

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return height(root) != -1