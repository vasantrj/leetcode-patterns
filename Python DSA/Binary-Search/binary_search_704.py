"""
Problem: Binary Search
LeetCode ID: 704
Pattern: Binary Search
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Maintain a search range using left and right pointers.
2. Check the middle element of the current range.
3. If the middle element equals the target, return its index.
4. If the middle element is smaller than the target,
   search the right half.
5. Otherwise, search the left half.
6. If the search range becomes empty, return -1.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    