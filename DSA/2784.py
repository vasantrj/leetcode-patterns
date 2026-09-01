"""
Problem: Check if Array is Good
LeetCode ID: 2784
Pattern: Arrays / Sorting
Difficulty: Easy
Time Complexity: O(n log n)
Space Complexity: O(1) extra

Approach:
1. A good array of length n must contain:
   [1, 2, 3, ..., n-1, n-1]
2. Sort the array.
3. Compare sorted nums with expected pattern.
4. Return True if they match, otherwise False.
"""

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        expected = list(range(1, n))
        expected.append(n - 1)
        return nums == expected
    