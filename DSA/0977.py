"""
Problem: Squares of a Sorted Array
LeetCode ID: 977
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use two pointers:
   - left at the start
   - right at the end
2. Compare absolute values of nums[left] and nums[right].
3. The larger absolute value gives the larger square.
4. Fill the result array from the end to the beginning.
5. Move the corresponding pointer inward.
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return result