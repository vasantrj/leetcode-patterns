"""
Problem: Counting Bits
LeetCode ID: 338
Pattern: Dynamic Programming / Bit Manipulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Let dp[i] represent number of set bits in i.
2. Observation:
   dp[i] = dp[i >> 1] + (i & 1)
3. Explanation:
   - i >> 1 removes the last bit
   - (i & 1) checks if last bit is 1
4. Build answer from 0 to n.
5. Return dp array.
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
    