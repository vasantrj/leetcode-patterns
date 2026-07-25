"""
Problem: Maximum Product of Two Digits
LeetCode ID: 3536
Pattern: Mathematics / Sorting
Difficulty: Easy

Time Complexity: O(d log d)
Space Complexity: O(d)

where d is the number of digits in n.

Approach:
1. Extract all digits from the integer.
2. Sort the digits in descending order.
3. Multiply the two largest digits.
4. Return the product.
"""

class Solution:
    def maxProduct(self, n: int) -> int:

        digits = sorted(
            (int(digit) for digit in str(n)),
            reverse=True
        )

        return digits[0] * digits[1]