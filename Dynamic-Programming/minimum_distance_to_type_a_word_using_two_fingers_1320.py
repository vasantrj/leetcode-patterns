"""
Problem: Minimum Distance to Type a Word Using Two Fingers
LeetCode ID: 1320
Pattern: Dynamic Programming
Difficulty: Hard
Time Complexity: O(26 * n)
Space Complexity: O(26)

Approach:
1. We simulate typing using two fingers on a keyboard grid.
2. Each character maps to a position in a 6-column grid.
3. Use DP where:
   dp[j] = minimum cost when:
     - one finger is at current character
     - other finger is at position j (0–25 or 26 for unused)
4. For each transition:
   - Move the same finger (cost = dist(cur, nxt))
   - Or move the other finger (cost = dist(j, nxt))
5. Use rolling DP to optimize space.
6. Return the minimum value in dp after processing all characters.
"""

class Solution(object):
    def minimumDistance(self, word):
        def dist(a, b):
            if a == 26: 
                return 0
            ra, ca = divmod(a, 6)
            rb, cb = divmod(b, 6)
            return abs(ra - rb) + abs(ca - cb)

        INF = float('inf')
        dp = [INF] * 27
        dp[26] = 0 

        for i in range(len(word) - 1):
            cur = ord(word[i]) - ord('A')
            nxt = ord(word[i + 1]) - ord('A')
            new_dp = [INF] * 27

            for j in range(27):
                if dp[j] == INF:
                    continue

                new_dp[j] = min(new_dp[j], dp[j] + dist(cur, nxt))
                new_dp[cur] = min(new_dp[cur], dp[j] + dist(j, nxt))

            dp = new_dp

        return min(dp)