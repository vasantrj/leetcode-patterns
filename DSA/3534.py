"""
Problem: Path Existence Queries in a Graph II
LeetCode ID: 3534
Pattern: Graphs / Binary Lifting
Difficulty: Hard

Time Complexity: O((n + q) log n)
Space Complexity: O(n log n)

where:
    n = number of nodes
    q = number of queries

Approach:
1. Sort the nodes according to their values in nums.
2. For every position, compute the farthest position that
   can be reached in one edge.
3. Build a binary lifting table where:
      lift[k][i] = farthest position reachable from i
                   after 2^k jumps.
4. For each query:
      - Convert node indices into their positions in the
        sorted order.
      - Use binary lifting to make the largest possible
        jumps without passing the target.
      - If one more jump reaches the target, return the
        minimum number of jumps; otherwise return -1.
"""

from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        val = [nums[i] for i in order]
        pos = [0] * n
        for i, o in enumerate(order):
            pos[o] = i

        right = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and val[j + 1] - val[i] <= maxDiff:
                j += 1
            right[i] = j

        LOG = max(1, n.bit_length() + 1)
        lift = [right]
        for k in range(1, LOG):
            prev = lift[-1]
            cur = [prev[prev[i]] for i in range(n)]
            lift.append(cur)

        ans = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if a == b:
                ans.append(0)
                continue
            lo, hi = (a, b) if a < b else (b, a)
            cur = lo
            jumps = 0
            for k in range(LOG - 1, -1, -1):
                nxt = lift[k][cur]
                if nxt < hi:
                    cur = nxt
                    jumps += (1 << k)
            if right[cur] >= hi:
                ans.append(jumps + 1)
            else:
                ans.append(-1)
        return ans