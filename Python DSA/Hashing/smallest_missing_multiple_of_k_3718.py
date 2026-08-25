"""
Problem: Smallest Missing Multiple of K
LeetCode ID: 3718
Pattern: Hash Set / Mathematics
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n)

where:
    n = length of nums
    m = number of consecutive multiples of k present in nums

Approach:
1. Store all elements of nums in a set for O(1) average lookup.
2. Start with the first positive multiple of k: k.
3. Keep increasing the candidate by k while it exists in the set.
4. The first missing candidate is the answer.
"""

from typing import List

class Solution:
    def missingMultiple(self,nums: List[int],k: int) -> int:
        numbers = set(nums)
        multiple = k
        while multiple in numbers:
            multiple += k
        return multiple
    