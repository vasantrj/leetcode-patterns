"""
Problem: Stone Game IV
LeetCode ID: 1510
Pattern: Dynamic Programming / Game Theory
Difficulty: Hard

Time Complexity: O(n * sqrt(n))
Space Complexity: O(n)

Approach:
1. Let dp[i] represent whether the current player can win
   when there are i stones remaining.
2. For every state i, try removing every perfect square
   j² <= i.
3. If removing j² leaves a losing state for the opponent,
   then the current state is winning.
4. If no such move exists, the current state is losing.
5. Return dp[n].
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]

        