"""
Problem: Jump Game II
LeetCode ID: 45
Pattern: Greedy
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use greedy BFS-like traversal.
2. Maintain:
   - current_end = farthest index reachable with current jumps
   - farthest = farthest index reachable overall
3. Traverse array:
   - Continuously update farthest
4. When reaching current_end:
   - must make another jump
   - update current_end = farthest
5. Return total jumps.
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps