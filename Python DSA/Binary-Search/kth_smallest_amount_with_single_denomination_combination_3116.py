"""
Problem: Kth Smallest Amount With Single Denomination Combination
LeetCode ID: 3116
Pattern: Binary Search / Inclusion-Exclusion / LCM
Difficulty: Hard

Time Complexity: O(2^n × n × log(min(coins) × k))
Space Complexity: O(1)

Approach:
1. Binary search for the smallest value x such that there
   are at least k valid amounts <= x.
2. Use Inclusion-Exclusion to count how many positive integers
   <= x are divisible by at least one coin.
3. For every subset of coins:
      - Compute its LCM.
      - Add x // LCM for subsets with odd size.
      - Subtract x // LCM for subsets with even size.
4. If count(x) >= k, search the left half.
5. Otherwise, search the right half.
"""

from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def count(x: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        c = coins[i]
                        g = gcd(lcm, c)
                        lcm = lcm // g * c
                        if lcm > x:
                            break
                if lcm > x:
                    continue
                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm
            return total
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
        