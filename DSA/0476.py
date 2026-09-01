"""
Problem: Number Complement
LeetCode ID: 476
Pattern: Bit Manipulation / Bitmask
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Create a mask containing the same number of bits as num,
   with every bit set to 1.
2. Start with mask = 1.
3. Keep extending the mask using:
      (mask << 1) | 1
4. XOR num with the mask to flip all bits of num.
5. Return the result.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) | 1
        return num ^ mask