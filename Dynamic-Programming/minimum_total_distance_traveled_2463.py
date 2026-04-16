"""
Problem: Minimum Total Distance Traveled
LeetCode ID: 2463
Pattern: Dynamic Programming / Sorting
Difficulty: Hard
Time Complexity: O(n * m * k)
Space Complexity: O(n * m)

Approach:
1. Sort robots and factories by position.
2. Use DP:
   dp[i][j] = minimum cost to assign first i robots using first j factories.
3. For each factory:
   - Either assign 0 robots to it
   - Or assign up to its capacity (k robots)
4. While assigning k robots:
   - Accumulate distance cost incrementally.
5. Return dp[n][m].
"""

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)
        INF = float('inf')

        dp = [[INF] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 0

        for j in range(1, m + 1):
            pos, lim = factory[j - 1]

            for i in range(n + 1):
                if dp[i][j - 1] < INF:
                    dp[i][j] = dp[i][j - 1]

                dist = 0
                for k in range(1, min(lim, i) + 1):
                    dist += abs(robot[i - k] - pos)

                    if dp[i - k][j - 1] < INF:
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + dist)

        return dp[n][m]