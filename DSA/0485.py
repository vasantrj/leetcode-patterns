"""
Problem: Max Consecutive Ones
LeetCode ID: 485
Pattern: Arrays / One-Pass
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain a counter for the current consecutive sequence of 1s.
2. When the current element is 1, increment the counter.
3. Update the maximum consecutive count.
4. When a 0 is encountered, reset the current counter to 0.
5. Return the maximum count found.
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0
        for n in nums:
            if n == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count