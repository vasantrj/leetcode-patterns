"""
Problem: Reverse Bits
LeetCode ID: 190
Pattern: Bit Manipulation
Difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Process all 32 bits of the integer.
2. Extract the bit at position i using:
      (n >> i) & 1
3. Place that bit at the mirrored position:
      31 - i
4. Combine all reversed bits using bitwise OR.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result |= bit << (31 - i)
        return result