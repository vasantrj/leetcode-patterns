"""
Problem: Find Minimum in Rotated Sorted Array II
LeetCode ID: 154
Pattern: Binary Search
Difficulty: Hard
Time Complexity: O(log n) average, O(n) worst case
Space Complexity: O(1)

Approach:
1. Array is sorted, rotated, and may contain duplicates.
2. Use binary search with three cases:
   - nums[mid] > nums[right]:
       minimum lies in right half
   - nums[mid] < nums[right]:
       minimum lies in left half including mid
   - nums[mid] == nums[right]:
       cannot determine side, shrink search space
3. Continue until left == right.
4. Return nums[left].
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
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
    