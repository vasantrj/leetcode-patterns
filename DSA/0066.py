"""
Problem: Plus One
LeetCode ID: 66
Pattern: Arrays / Simulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1) extra

Approach:
1. Traverse digits from right to left.
2. If digit is less than 9:
   - Increment it and return.
3. Otherwise:
   - Set digit to 0 and continue carry.
4. If all digits become 0:
   - Insert 1 at the beginning.
5. Return resulting array.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits