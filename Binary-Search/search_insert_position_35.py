"""
Problem: Search Insert Position
LeetCode ID: 35
Pattern: Binary Search
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Use binary search on the sorted array.
2. If target is found:
   - return its index.
3. Otherwise:
   - return the position where it should be inserted
     to maintain sorted order.
4. The insertion position is the final left pointer.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    