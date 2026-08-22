"""
Problem: Smallest Even Multiple
LeetCode ID: 2413
Pattern: Mathematics
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. If n is already even, n itself is the smallest even multiple.
2. If n is odd, 2 * n is the smallest even multiple.
"""


class Solution:
    def smallestEvenMultiple(self,n: int) -> int:
        return n if n % 2 == 0 else n * 2