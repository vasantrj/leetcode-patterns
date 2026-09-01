"""
Problem: Find First and Last Position of Element in Sorted Array
LeetCode ID: 34
Pattern: Binary Search
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Use binary search twice:
   - First occurrence of target
   - Last occurrence of target
2. For first occurrence:
   - continue searching left half after finding target
3. For last occurrence:
   - continue searching right half after finding target
4. Return [first, last].
5. If target not found, return [-1, -1].
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first() -> int:
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def find_last() -> int:
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [find_first(), find_last()]