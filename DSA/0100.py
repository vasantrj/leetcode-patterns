"""
Problem: Same Tree
LeetCode ID: 100
Pattern: Binary Tree, Recursion, Depth-First Search
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. If both nodes are None, the corresponding subtrees are identical.
2. If only one node is None, the trees are different.
3. If the node values differ, the trees are different.
4. Recursively compare the left and right subtrees.

Key Insight:
Two binary trees are identical only when their root values match and
their corresponding left and right subtrees are also identical.
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)