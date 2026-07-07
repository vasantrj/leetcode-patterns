"""
Problem: Concatenate Non-Zero Digits and Multiply by Sum I
LeetCode ID: 3754
Pattern: Strings / Simulation
Difficulty: Easy

Time Complexity: O(d)
Space Complexity: O(d)

where:
    d = number of digits in n

Approach:
1. Convert the number to a string.
2. Remove all '0' digits.
3. If no non-zero digits remain, return 0.
4. Concatenate the remaining digits to form a new number.
5. Compute the sum of the remaining digits.
6. Return the product of the concatenated number and the digit sum.
"""

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [d for d in str(n) if d != '0']
        if not digits:
            return 0
        x = int(''.join(digits))
        s = sum(int(d) for d in digits)
        return x * s
        