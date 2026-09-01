"""
Problem: Stone Game
LeetCode ID: 877
Pattern: Dynamic Programming / Game Theory
Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n²)

Approach:
1. Let dp[i][j] represent the maximum score difference
   (current player - opponent) obtainable from the
   subarray piles[i...j].
2. If only one pile remains, the current player takes it:
      dp[i][i] = piles[i]
3. For every larger subarray:
      - Pick the left pile:
            piles[i] - dp[i + 1][j]
      - Pick the right pile:
            piles[j] - dp[i][j - 1]
4. Store the better of the two choices.
5. If the final score difference is positive,
   Alice collects more stones than Bob, so return True.
"""

from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        return dp[0][n - 1] > 0
        