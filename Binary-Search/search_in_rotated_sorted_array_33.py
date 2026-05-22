"""
Problem: Search in Rotated Sorted Array
LeetCode ID: 33
Pattern: Binary Search
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Use binary search on the rotated sorted array.
2. At every step:
   - One half is always sorted.
3. Check whether target lies inside the sorted half:
   - If yes → search there
   - Otherwise → search the other half
4. Continue until target is found or search space becomes empty.
5. Return index if found, otherwise -1.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    