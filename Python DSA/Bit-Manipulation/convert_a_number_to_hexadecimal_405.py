"""
Problem: Convert a Number to Hexadecimal
LeetCode ID: 405
Pattern: Bit Manipulation / Number System
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(log n)

Approach:
1. Handle 0 as a special case.
2. For negative numbers, convert them to their
   32-bit unsigned representation.
3. Repeatedly extract the hexadecimal digit using
   modulo 16.
4. Divide the number by 16 to process the next digit.
5. Reverse the collected digits to obtain the final result.
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = "0123456789abcdef"
        if num < 0:
            num += 2 ** 32
        result = []
        while num > 0:
            result.append(digits[num % 16])
            num //= 16
        return "".join(reversed(result))

        