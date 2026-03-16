"""
Problem: Remove Duplicates from Sorted Array
LeetCode ID: 26
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - i tracks the position of the last unique element.
   - j scans through the array.
2. When nums[j] != nums[i], move i forward and update nums[i].
3. Continue until the end of the array.
4. The number of unique elements is i + 1.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1