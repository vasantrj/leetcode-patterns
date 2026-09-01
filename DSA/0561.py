"""
Problem: Array Partition
LeetCode ID: 561
Pattern: Greedy / Sorting
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort the array in non-decreasing order.
2. Pair adjacent elements after sorting.
3. In each pair, the smaller element contributes to the answer.
4. Sum every alternate element starting from index 0.
"""

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
    