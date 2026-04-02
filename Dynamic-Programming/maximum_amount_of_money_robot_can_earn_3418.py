"""
Problem: Maximum Amount of Money Robot Can Earn
LeetCode ID: 3418
Pattern: Dynamic Programming / Grid DP
Difficulty: Medium
Time Complexity: O(m * n * 3)
Space Complexity: O(m * n * 3)

Approach:
1. The robot starts at the top-left and moves only right or down.
2. Each cell contains either:
   - positive coins → collect them
   - negative coins → lose money unless neutralized
3. The robot can neutralize the effect of at most 2 negative cells.
4. Use DP where:
   dp[i][j][k] = maximum money collected when reaching cell (i, j)
                  using exactly k neutralizations.
5. Transition from top or left:
   - Take the cell value normally
   - If current cell is negative and k > 0, optionally neutralize it
6. Final answer is the maximum among dp[m-1][n-1][0..2].
"""

from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')
        # dp[i][j][k] = max money at cell (i, j) using k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        # Initialize start cell
        start = coins[0][0]
        dp[0][0][0] = start
        if start < 0:
            dp[0][0][1] = 0  # neutralize first negative cell
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == NEG_INF:
                        continue
                    # Move Down
                    if i + 1 < m:
                        val = coins[i + 1][j]
                        # Take value normally
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + val)
                        # Neutralize if negative and possible
                        if val < 0 and k < 2:
                            dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k])
                    # Move Right
                    if j + 1 < n:
                        val = coins[i][j + 1]
                        # Take value normally
                        dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k] + val)
                        # Neutralize if negative and possible
                        if val < 0 and k < 2:
                            dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k])
        return max(dp[m - 1][n - 1])