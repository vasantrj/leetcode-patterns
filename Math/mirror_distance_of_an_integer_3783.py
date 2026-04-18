"""
Problem: Mirror Distance of an Integer
LeetCode ID: 3783
Pattern: Math / Number Manipulation
Difficulty: Easy
Time Complexity: O(d)  (d = number of digits)
Space Complexity: O(1)

Approach:
1. Reverse the digits of the integer.
2. Compute absolute difference between original and reversed number.
3. Return the result.

Note:
- Two methods exist:
  1) String reversal
  2) Mathematical reversal (used below for optimal space)
"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))

        # ----- OR -----

class Solution:
    def mirrorDistance(self, n: int) -> int:
        x, y = n, 0

        while x:
            y = y * 10 + x % 10
            x //= 10

        return abs(n - y)