"""
Problem: Power of Three
LeetCode ID: 326
Pattern: Mathematics / Repeated Division
Difficulty: Easy

Time Complexity: O(log₃ n)
Space Complexity: O(1)

Approach:
1. A power of three must be positive.
2. Repeatedly divide n by 3 while it is divisible by 3.
3. If the final value is 1, the original number was a
   power of three.
4. Otherwise, it contained a factor other than 3.
"""


class Solution:
    def isPowerOfThree(self,n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1