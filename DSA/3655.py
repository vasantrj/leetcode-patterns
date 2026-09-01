"""
Problem: XOR After Range Multiplication Queries II
LeetCode ID: 3655
Pattern: Math / Sqrt Decomposition
Difficulty: Hard
Time Complexity: O(q * sqrt(n) + n * sqrt(n))
Space Complexity: O(n * sqrt(n)) in sparse form

Approach:
1. Each query is of the form [l, r, k, v]:
   - Multiply nums[l], nums[l+k], nums[l+2k], ... <= r by v
2. Direct simulation is too slow for large inputs.
3. Use sqrt decomposition:
   - Let B ≈ sqrt(n)
4. For queries:
   - If k >= B:
     - Number of updated positions is small, so update directly.
   - If k < B:
     - Use sparse multiplicative difference arrays.
5. For small k:
   - Store start multiplier at l
   - Store inverse multiplier at (last + k)
   - Later apply all updates in one prefix-product scan for each residue class.
6. Finally, compute XOR of the updated array.
"""

from math import isqrt
from functools import reduce
from operator import xor
from collections import defaultdict
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = max(1, isqrt(n))  # block size ≈ √n

        # Sparse multiplicative difference arrays for small k
        mdiff = [defaultdict(lambda: 1) for _ in range(B)]

        for l, r, k, v in queries:
            if k >= B:
                # Large step: direct update
                for idx in range(l, r + 1, k):
                    nums[idx] = nums[idx] * v % MOD
            else:
                # Small step: difference array update
                last = l + ((r - l) // k) * k
                inv_v = pow(v, MOD - 2, MOD)

                mdiff[k][l] = mdiff[k][l] * v % MOD
                mdiff[k][last + k] = mdiff[k][last + k] * inv_v % MOD

        # Apply all pending small-step updates
        for k in range(1, B):
            if not mdiff[k]:
                continue

            dk = mdiff[k]

            for r0 in range(k):
                running = 1
                pos = r0

                while pos < n:
                    m = dk.get(pos, 1)
                    if m != 1:
                        running = running * m % MOD

                    if running != 1:
                        nums[pos] = nums[pos] * running % MOD

                    pos += k

        return reduce(xor, nums)