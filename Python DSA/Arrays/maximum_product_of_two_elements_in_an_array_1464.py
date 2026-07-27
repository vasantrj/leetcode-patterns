"""
Problem: Maximum Product of Two Elements in an Array
LeetCode ID: 1464
Pattern: Arrays / Greedy
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the array once.
2. Keep track of the largest and second largest elements.
3. Update them whenever a larger element is found.
4. Return (largest - 1) × (second largest - 1).
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for n in nums:
            if n > first:
                first, second = n, first
            elif n > second:
                second = n
        return (first - 1) * (second - 1)