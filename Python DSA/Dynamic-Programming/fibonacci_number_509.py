"""
Problem: Fibonacci Number
LeetCode ID: 509
Pattern: Dynamic Programming / Iteration
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Handle n = 0 separately.
2. Maintain two variables:
      - a = previous Fibonacci number
      - b = current Fibonacci number
3. Update them iteratively using:
      a, b = b, a + b
4. After n - 1 iterations, b contains F(n).
"""


class Solution:
    def fib(self,n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b