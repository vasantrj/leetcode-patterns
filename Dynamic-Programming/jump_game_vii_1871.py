"""
Problem: Jump Game VII
LeetCode ID: 1871
Pattern: Dynamic Programming / Sliding Window
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Let dp[i] = True if index i is reachable.
2. Start with dp[0] = True.
3. Maintain a sliding window count of reachable positions:
   - positions in [i - maxJump, i - minJump]
4. If:
   - s[i] == '0'
   - and at least one reachable index exists in window
     then dp[i] = True
5. Return dp[n-1].
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        reachable = 0
        for i in range(1, n):

            # Add new index entering window
            if i >= minJump and dp[i - minJump]:
                reachable += 1

            # Remove old index leaving window
            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1

            # Current index reachable
            if s[i] == '0' and reachable > 0:
                dp[i] = True
        return dp[-1]