"""
Problem: Find Greatest Common Divisor of Array
LeetCode ID: 1979
Pattern: Mathematics / GCD
Difficulty: Easy

Time Complexity: O(n + log(max(nums)))
Space Complexity: O(1)

Approach:
1. Find the minimum and maximum elements in the array.
2. Compute the GCD of these two values.
3. Return the result.
"""

from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))