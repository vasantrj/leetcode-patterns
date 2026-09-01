"""
Problem: Stone Game III
LeetCode ID: 1406
Pattern: Dynamic Programming / Game Theory
Difficulty: Hard

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Let dp[i] represent the maximum score difference
   (current player - opponent) starting from index i.
2. At each position, the current player can take
   1, 2, or 3 stones.
3. For each choice:
      - Compute the sum of the taken stones.
      - Subtract the opponent's best score difference
        from the remaining stones.
4. Store the maximum score difference.
5. If:
      - dp[0] > 0  → Alice wins.
      - dp[0] < 0  → Bob wins.
      - dp[0] == 0 → Tie.
"""

from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1) 
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                total += stoneValue[i + k - 1]
                best = max(best, total - dp[i + k])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        