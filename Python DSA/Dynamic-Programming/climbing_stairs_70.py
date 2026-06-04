"""
Problem: Climbing Stairs
LeetCode ID: 70
Pattern: Dynamic Programming / Fibonacci
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. At each step, you can reach it from:
   - one step before
   - two steps before
2. This forms a Fibonacci relation:
   dp[i] = dp[i-1] + dp[i-2]
3. Use two variables to store previous results:
   - a = dp[i-2]
   - b = dp[i-1]
4. Iterate and update values.
5. Return final result.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for _ in range(n - 1):
            a, b = b, a + b

        return b