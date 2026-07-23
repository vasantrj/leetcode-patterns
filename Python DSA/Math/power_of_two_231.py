"""
Problem: Power of Two
LeetCode ID: 231
Pattern: Bit Manipulation
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. A power of two has exactly one bit set in its binary representation.
2. For any positive power of two n:
      n & (n - 1) == 0
3. First ensure n is positive, then apply the bitwise check.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

    