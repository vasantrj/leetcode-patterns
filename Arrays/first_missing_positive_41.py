"""
Problem: First Missing Positive
LeetCode ID: 41
Pattern: Array / Cyclic Sort
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The smallest missing positive must be in the range [1, n+1].
2. Place each number at its correct index:
   number x should be placed at index x-1.
3. Swap elements until each valid number is in its correct position.
4. Scan the array:
   - If nums[i] != i + 1, then i + 1 is the missing number.
5. If all numbers are correct, return n + 1.
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while (
                1 <= nums[i] <= n and
                nums[nums[i] - 1] != nums[i]
            ):
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1