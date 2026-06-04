"""
Problem: Jump Game V
LeetCode ID: 1340
Pattern: Dynamic Programming / DFS Memoization
Difficulty: Hard
Time Complexity: O(n * d)
Space Complexity: O(n)

Approach:
1. Treat each index as a node in a DAG:
   - You can only jump to strictly smaller values.
2. Use DFS + memoization:
   dfs(i) = maximum indices visitable starting from i.
3. From index i:
   - Explore right within distance d
   - Explore left within distance d
4. Stop exploring in a direction if:
   arr[j] >= arr[i]
   because jumps beyond become invalid.
5. Memoize results to avoid recomputation.
6. Try all starting indices and return maximum.
"""

from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]
            max_jumps = 1

            # Jump right
            for j in range(i + 1, min(i + d + 1, len(arr))):
                if arr[j] >= arr[i]:
                    break

                max_jumps = max(max_jumps, 1 + dfs(j))

            # Jump left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break

                max_jumps = max(max_jumps, 1 + dfs(j))
            memo[i] = max_jumps
            return max_jumps
        result = 0
        for i in range(len(arr)):
            result = max(result, dfs(i))
        return result