"""
Problem: Missing Number
LeetCode ID: 268
Pattern: Array / Math
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The numbers range from 0 to n.
2. The expected sum of numbers from 0 to n is:
   n * (n + 1) // 2
3. Compute the actual sum of the array.
4. The missing number is the difference between the expected sum and the actual sum.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum