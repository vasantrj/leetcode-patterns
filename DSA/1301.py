"""
Problem: Number of Paths with Max Score
LeetCode ID: 1301
Pattern: Dynamic Programming
Difficulty: Hard

Time Complexity: O(n²)
Space Complexity: O(n²)

Approach:
1. Use dynamic programming where each cell stores:
      (maximum score, number of ways).
2. Start from the bottom-right ('S') with:
      (0, 1)
3. Traverse the board from bottom-right to top-left.
4. For each cell:
      - Ignore blocked cells ('X').
      - Consider the three reachable neighbors:
            • Down
            • Right
            • Down-Right
      - Choose the maximum score among them.
      - Sum the number of ways for all neighbors
        achieving that maximum score.
      - Add the current cell's value
        (0 for 'E', digit otherwise).
5. The answer is stored at the top-left ('E').
   If unreachable, return [0, 0].
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == n-1 and j == n-1:
                    continue
                if board[i][j] == 'X':
                    dp[i][j] = (-1, 0)
                    continue
                
                best = -1
                cnt = 0
                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and dp[ni][nj][0] >= 0:
                        s, c = dp[ni][nj]
                        if s > best:
                            best = s
                            cnt = c
                        elif s == best:
                            cnt = (cnt + c) % MOD
                
                if best < 0:
                    dp[i][j] = (-1, 0)
                else:
                    val = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp[i][j] = (best + val, cnt)
        
        score, count = dp[0][0]
        if score < 0:
            return [0, 0]
        return [score, count]

        