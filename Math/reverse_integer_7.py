"""
Problem: Reverse Integer
LeetCode ID: 7
Pattern: Math / Number Manipulation
Difficulty: Medium
Time Complexity: O(log10(n))
Space Complexity: O(1)

Approach:
1. Extract digits using modulo 10.
2. Build reversed number by multiplying current result by 10 and adding digit.
3. Handle negative numbers by storing sign.
4. Check for 32-bit integer overflow:
   - range: [-2^31, 2^31 - 1]
5. If overflow occurs, return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        rev *= sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev

