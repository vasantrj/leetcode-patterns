"""
Problem: Symmetric Tree
LeetCode ID: 101
Pattern: Binary Tree, Recursion, DFS
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Compare the tree with itself using a recursive mirror check.
2. For two mirror nodes, verify that their values are equal.
3. Recursively compare the left subtree of one node with the right
   subtree of the other, and vice versa.
4. If both subtrees satisfy the mirror condition, the tree is symmetric.

"""


from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root, root)