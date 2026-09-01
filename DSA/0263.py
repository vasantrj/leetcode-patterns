"""
Problem: Ugly Number
LeetCode ID: 263
Pattern: Mathematics / Prime Factorization
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. An ugly number is a positive integer whose prime factors
   are only 2, 3, and 5.
2. Repeatedly divide n by 2, 3, and 5 while they divide n.
3. If only 1 remains, n had no other prime factors.
4. Otherwise, n contains a prime factor other than 2, 3, or 5.
"""

class Solution:
    def isUgly(self,n: int) -> bool:
        if n <= 0:
            return False
        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor
        return n == 1