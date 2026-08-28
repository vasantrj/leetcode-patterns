"""
Problem: Base 7
LeetCode ID: 504
Pattern: Math / Number System / Digit Manipulation
Difficulty: Easy

Time Complexity: O(log₇ n)
Space Complexity: O(log₇ n)

Approach:
1. Handle zero separately.
2. Store whether the number is negative.
3. Work with the absolute value.
4. Repeatedly divide the number by 7:
      - num % 7 gives the current base-7 digit.
      - num //= 7 removes that digit.
5. The digits are generated from right to left, so reverse them.
6. Add the negative sign if the original number was negative.
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
        
        result = ''.join(reversed(digits))
        return '-' + result if negative else result