"""
Problem: Stone Game VIII
LeetCode ID: 1872
Pattern: Dynamic Programming / Prefix Sum / Game Theory
Difficulty: Hard

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build a prefix sum array where prefix[i] represents
   the sum of stones from index 0 to i.
2. Define dp[i] as the maximum score difference the current
   player can achieve starting from prefix[i].
3. For each position from right to left:
      - Skip the current prefix: dp[i + 1]
      - Take the current prefix: prefix[i] - dp[i + 1]
4. Take the better of these two choices.
5. The game must make the first move using at least two stones,
   so the final answer is dp[1].
"""

from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
        
        dp = [0] * n
        dp[n - 1] = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            option_skip = dp[i + 1]
            option_take = prefix[i] - dp[i + 1]
            dp[i] = max(option_skip, option_take)
        return dp[1]