"""
Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
LeetCode ID: 2996
Pattern: Arrays / Hash Set
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Find the longest sequential prefix where every element
   is exactly one greater than the previous element.
2. Calculate the sum of this sequential prefix.
3. Store all numbers in a set for O(1) average lookup.
4. If the prefix sum already exists in the array, keep
   increasing it until a missing integer is found.
5. Return the first missing integer.
"""

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] == nums[i-1] + 1:
            i += 1
        s = sum(nums[:i])
        num_set = set(nums)
        while s in num_set:
            s += 1
        return s

        