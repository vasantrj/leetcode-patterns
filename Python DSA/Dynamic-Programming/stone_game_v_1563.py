"""
Problem: Stone Game V
LeetCode ID: 1563
Pattern: Dynamic Programming / Prefix Sum / Game Theory
Difficulty: Hard

Time Complexity: O(n²)
Space Complexity: O(n²)

Approach:
1. Build a prefix sum array to calculate the sum of any
   subarray in O(1).
2. Let dp[i][j] represent the maximum score Alice can obtain
   from stoneValue[i...j].
3. Split the interval at position k into:
      left  = stoneValue[i...k]
      right = stoneValue[k+1...j]
4. If left < right, Alice keeps the left part.
5. If left > right, Alice keeps the right part.
6. If left == right, Alice can choose either side.
7. Use monotonic pointers to avoid checking every possible
   split repeatedly, reducing the solution to O(n²).
"""

from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        def rsum(i, j):
            return prefix[j + 1] - prefix[i]
        dp = [[0] * n for _ in range(n)]
        kR = [j + 1 for j in range(n)]
        bestR = [0] * n
        for i in range(n - 1, -1, -1):
            k = i - 1 
            bestL = 0
            for j in range(i + 1, n):
                total = rsum(i, j)
                while k + 1 <= j - 1 and 2 * rsum(i, k + 1) <= total:
                    k += 1
                    bestL = max(bestL, dp[i][k] + rsum(i, k))
                while kR[j] - 1 >= i + 1 and 2 * rsum(kR[j] - 1, j) <= total:
                    kR[j] -= 1
                    bestR[j] = max(bestR[j], dp[kR[j]][j] + rsum(kR[j], j))
                dp[i][j] = max(bestL, bestR[j])
        return dp[0][n - 1]