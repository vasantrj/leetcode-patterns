"""
Problem: Maximum Number of Jumps to Reach the Last Index
LeetCode ID: 2770
Pattern: Dynamic Programming
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(n)

Approach:
1. Let dp[i] = maximum jumps needed to reach index i.
2. Initialize:
   - dp[0] = 0
   - all others = -1 (unreachable)
3. For every pair (j, i):
   - If index j is reachable
   - And abs(nums[i] - nums[j]) <= target
     then we can jump from j -> i
4. Update:
   dp[i] = max(dp[i], dp[j] + 1)
5. Return dp[n-1].
"""

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]