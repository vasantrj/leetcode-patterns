"""
Problem: Third Maximum Number
LeetCode ID: 414
Pattern: Arrays / One-Pass
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain the three largest distinct numbers:
      - first  -> largest
      - second -> second largest
      - third  -> third largest
2. Ignore duplicate values.
3. When a new value becomes the largest, shift the
   existing values down.
4. Otherwise, update the second or third maximum when needed.
5. If a third distinct maximum does not exist, return
   the largest value.
"""

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None\
        for n in nums:
            if n in (first, second, third):
                continue
            if first is None or n > first:
                first, second, third = n, first, second
            elif second is None or n > second:
                second, third = n, second
            elif third is None or n > third:
                third = n
        return third if third is not None else first
        