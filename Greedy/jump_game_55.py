"""
Problem: Jump Game
LeetCode ID: 55
Pattern: Greedy
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain the farthest index reachable so far.
2. Traverse the array:
   - If current index is beyond reachable range,
     return False.
   - Update farthest reachable position.
3. If traversal completes, last index is reachable.
4. Return True.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True
    
    