"""
Problem: Maximum Product of Three Numbers
LeetCode ID: 628
Pattern: Arrays / Sorting
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort the array in ascending order.
2. The maximum product can come from:
      - The three largest numbers.
      - The two smallest numbers (possibly negative)
        multiplied by the largest number.
3. Return the maximum of these two possibilities.
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )