"""
Problem: XOR After Range Multiplication Queries I
LeetCode ID: 3653
Pattern: Math / Simulation
Difficulty: Medium
Time Complexity: O(total updates)
Space Complexity: O(1)

Approach:
1. Each query is of the form [l, r, k, v]:
   - Start from index l
   - Jump by k steps
   - Multiply nums[idx] by v while idx <= r
2. Apply modulo (10^9 + 7) after each multiplication.
3. After all queries, compute XOR of all elements.
4. Use reduce + xor for concise computation.
"""

from functools import reduce
from operator import xor
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        return reduce(xor, nums)