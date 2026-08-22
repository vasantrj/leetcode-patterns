"""
Problem: Check Divisibility by Digit Sum and Product
LeetCode ID: 3622
Pattern: Mathematics / Digit Manipulation
Difficulty: Easy

Time Complexity: O(d)
Space Complexity: O(1)

where:
    d = number of digits in n

Approach:
1. Convert n into its individual digits.
2. Calculate the sum of all digits.
3. Calculate the product of all digits.
4. Add the digit sum and digit product.
5. Check whether n is divisible by this value.
"""

class Solution:
    def checkDivisibility(
        self,
        n: int
    ) -> bool:

        digit_sum = 0
        digit_product = 1

        for character in str(n):

            digit = int(character)

            digit_sum += digit
            digit_product *= digit

        return (
            n % (digit_sum + digit_product) == 0
        )