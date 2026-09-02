"""
Problem: Path Sum
LeetCode ID: 112
Pattern: Binary Tree, DFS, Recursion
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Return False if the tree is empty.
2. If the current node is a leaf, check whether its value equals
   the remaining target sum.
3. Subtract the current node's value from the target sum.
4. Recursively check the left and right subtrees with the remaining sum.
5. Return True if either subtree contains a valid root-to-leaf path.

"""


from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))