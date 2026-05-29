"""
Problem: Minimum Element After Replacement With Digit Sum
LeetCode ID: 3300
Pattern: Arrays / Math
Difficulty: Easy
Time Complexity: O(n * d)
Space Complexity: O(1)

Approach:
1. Replace each number with the sum of its digits.
2. Track the minimum digit sum encountered.
3. Return the minimum value.
"""

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total
        return min(digit_sum(num) for num in nums)
    