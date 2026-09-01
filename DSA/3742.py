"""
Problem: Maximum Path Score in a Grid
LeetCode ID: 3742
Pattern: Dynamic Programming / Grid / Knapsack-like
Difficulty: Medium
Time Complexity: O(m * n * k)
Space Complexity: O(m * n * k)

Approach:
1. Use DP where each cell stores:
   dp[i][j][cost] = max score achievable reaching (i, j) with given cost.
2. Initialize:
   dp[0][0] = {0: 0}
3. For each cell:
   - Try moving right and down.
   - Compute added cost and score based on grid value:
     0 → (0 cost, 0 score)
     1 → (1 cost, 1 score)
     2 → (1 cost, 2 score)
4. Only keep states where cost ≤ k.
5. At each cell, keep only the best score for each cost.
6. Answer = max score at (m-1, n-1), else -1.
"""

from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[{} for _ in range(n)] for _ in range(m)]
        dp[0][0] = {0: 0}

        for i in range(m):
            for j in range(n):
                for cost_so_far, score_so_far in list(dp[i][j].items()):

                    for ni, nj in [(i + 1, j), (i, j + 1)]:
                        if ni >= m or nj >= n:
                            continue

                        val = grid[ni][nj]

                        if val == 0:
                            add_cost, add_score = 0, 0
                        elif val == 1:
                            add_cost, add_score = 1, 1
                        else:
                            add_cost, add_score = 1, 2

                        new_cost = cost_so_far + add_cost
                        if new_cost > k:
                            continue

                        new_score = score_so_far + add_score

                        if new_cost not in dp[ni][nj] or dp[ni][nj][new_cost] < new_score:
                            dp[ni][nj][new_cost] = new_score

        if not dp[m - 1][n - 1]:
            return -1

        return max(dp[m - 1][n - 1].values())
    