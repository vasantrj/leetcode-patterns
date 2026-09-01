"""
Problem: Stone Game II
LeetCode ID: 1140
Pattern: Dynamic Programming / Game Theory / Memoization
Difficulty: Medium

Time Complexity: O(n^3)
Space Complexity: O(n^2)

Approach:
1. Build a suffix sum array so the total stones remaining
   from any position can be obtained in O(1).
2. Define dp(i, M) as the maximum number of stones the
   current player can collect starting from index i with
   the current limit M.
3. The player can take between 1 and 2 * M piles.
4. After taking x piles, the next state becomes:
      dp(i + x, max(M, x))
5. Use memoization to avoid recalculating states.
6. If the player can take all remaining piles, return the
   total remaining stones immediately.
"""

from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, M: int) -> int:
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            best = 0
            for x in range(1, 2 * M + 1):
                best = max(best, suffix_sum[i] - dp(i + x, max(M, x)))
            return best

        return dp(0, 1)
    