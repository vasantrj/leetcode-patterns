"""
Problem: Single Number
LeetCode ID: 136
Pattern: Bit Manipulation / XOR
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize the result as 0.
2. XOR every element in the array with the result.
3. Duplicate numbers cancel each other because:
      a ^ a = 0
4. The remaining value is the number that appears only once.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result