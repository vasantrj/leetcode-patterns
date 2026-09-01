"""
Problem: Number of Unique XOR Triplets I
LeetCode ID: 3513
Pattern: Bit Manipulation / Mathematics
Difficulty: Medium

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. If the array has fewer than 3 elements, every element
   itself forms a unique XOR value, so return n.
2. Otherwise, let k be the highest set bit needed to
   represent n.
3. The number of distinct XOR values equals the next
   power of two greater than n, which is:
      2^(⌊log₂(n)⌋ + 1)
4. Return this value.
"""

import math
from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << (int(math.log2(n)) + 1)
    