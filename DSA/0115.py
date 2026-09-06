"""
Problem: Distinct Subsequences
LeetCode ID: 115
Pattern: Dynamic Programming / String
Difficulty: Hard
Time Complexity: O(m * n)
Space Complexity: O(n)

Approach:
1. Let dp[j] represent the number of distinct subsequences of the
   processed part of s that form the first j characters of t.
2. Initialize dp[0] = 1 because there is exactly one way to form an
   empty string: by choosing no characters.
3. Traverse s from left to right.
4. For each character s[i - 1], traverse t from right to left:
   - If s[i - 1] == t[j - 1], we can use the current character of s
     to extend all subsequences that previously formed t[:j - 1].
   - Therefore, update dp[j] += dp[j - 1].
5. Traverse j backwards so that dp[j - 1] still represents the
   previous state from before processing the current character of s.
6. After processing all characters of s, dp[n] contains the number of
   distinct subsequences of s that equal t.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]