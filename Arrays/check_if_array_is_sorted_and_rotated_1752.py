"""
Problem: Check if Array Is Sorted and Rotated
LeetCode ID: 1752
Pattern: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. In a sorted and rotated array:
   there can be at most one "drop"
   where nums[i] > nums[(i+1) % n]
2. Traverse the array circularly.
3. Count number of drops.
4. If drops <= 1:
   array is sorted and rotated.
5. Otherwise return False.
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
        return drops <= 1
        