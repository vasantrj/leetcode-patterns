"""
Problem: Find Minimum in Rotated Sorted Array
LeetCode ID: 153
Pattern: Binary Search
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. The array is sorted then rotated.
2. Minimum element lies in the unsorted half.
3. Use binary search:
   - Compare nums[mid] with nums[right]
4. Cases:
   - nums[mid] > nums[right]:
       minimum is in right half
   - otherwise:
       minimum is in left half including mid
5. Continue until left == right.
6. Return nums[left].
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
    