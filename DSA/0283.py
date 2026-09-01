"""
Problem: Move Zeroes
LeetCode ID: 283
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - left → position to place the next non-zero element
   - right → scans the array
2. If nums[right] is non-zero:
   - Swap nums[left] and nums[right]
   - Move left forward
3. Continue until the end of the array.
4. This keeps all non-zero elements in order and pushes zeroes to the end.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1