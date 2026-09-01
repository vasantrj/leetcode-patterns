"""
Problem: Sequential Digits
LeetCode ID: 1291
Pattern: Backtracking / Enumeration
Difficulty: Medium

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Use the string "123456789" as the source of all
   possible sequential numbers.
2. Determine the minimum and maximum digit lengths
   based on the given range.
3. Generate every substring of valid lengths.
4. Convert each substring into an integer.
5. Keep only the numbers that lie within [low, high].
"""

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        n_low, n_high = len(str(low)), len(str(high))
        result = []
        
        for length in range(n_low, n_high + 1):
            for start in range(0, len(digits) - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        
        return result
    