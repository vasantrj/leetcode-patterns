"""
Problem: Predict the Winner
LeetCode ID: 486
Pattern: Dynamic Programming / Game Theory
Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n²)

Approach:
1. Let dp[i][j] represent the maximum score difference
   (current player - opponent) obtainable from the
   subarray nums[i...j].
2. If only one number remains, the current player takes it:
      dp[i][i] = nums[i]
3. For every larger subarray:
      - Pick the left number:
            nums[i] - dp[i + 1][j]
      - Pick the right number:
            nums[j] - dp[i][j - 1]
4. Store the better of the two choices.
5. If the final score difference is non-negative,
   Player 1 can guarantee at least a tie, so return True.
"""

from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        return dp[0][n - 1] >= 0