"""
Problem: Find Pivot Index
LeetCode ID: 724
Pattern: Arrays / Prefix Sum
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Calculate the total sum of the array.
2. Maintain the sum of elements to the left of the current index.
3. The right sum can be calculated as:
      total_sum - left_sum - current_element
4. If left_sum equals right_sum, the current index is the
   pivot index.
5. Return the first pivot index found.
6. If no pivot index exists, return -1.
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1
        