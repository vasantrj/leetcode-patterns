"""
Problem: Binary Number with Alternating Bits
LeetCode ID: 693
Pattern: Bit Manipulation
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. XOR n with n shifted right by one position:
   - x = n ^ (n >> 1)
   - If n has alternating bits, every adjacent pair of bits is
     different, so all relevant bits in x become 1.
2. A number consisting of consecutive 1s has the binary form
   111...111.
3. For such a number x, x + 1 has the form 1000...000.
4. Therefore, x & (x + 1) == 0 if and only if x consists entirely
   of consecutive 1s.
5. Return whether this condition is satisfied.
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0