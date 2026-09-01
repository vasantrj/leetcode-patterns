"""
Problem: Number of Unique XOR Triplets II
LeetCode ID: 3514
Pattern: Bit Manipulation / Hash Set
Difficulty: Medium

Time Complexity: O(u² + u × p)
Space Complexity: O(p)

where:
    u = number of unique elements
    p = number of distinct pair XOR values

Approach:
1. Remove duplicate numbers since repeated values do not
   create new XOR results.
2. Compute all possible XOR values of pairs (including
   pairing an element with itself).
3. XOR every pair XOR value with every unique number.
4. Store the results in a set to keep only distinct
   triplet XOR values.
5. Return the number of unique XOR values.
"""

from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq = list(set(nums))
        n = len(uniq)
        
        pair_xor = set()
        for idx in range(n):
            a = uniq[idx]
            for jdx in range(idx, n):
                pair_xor.add(a ^ uniq[jdx])
        
        result = {x ^ y for x in pair_xor for y in uniq}
        return len(result)