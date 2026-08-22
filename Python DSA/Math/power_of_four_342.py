"""
Problem: Power of Four
LeetCode ID: 342
Pattern: Mathematics / Repeated Division
Difficulty: Easy

Time Complexity: O(log₄ n)
Space Complexity: O(1)

Approach:
1. A power of four must be positive.
2. Repeatedly divide n by 4 while it is divisible by 4.
3. If the final value is 1, the original number was a
   power of four.
4. Otherwise, n contains factors other than 4.
"""


class Solution:
    def isPowerOfFour(self,n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1