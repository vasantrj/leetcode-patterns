"""
Problem: Count the Digits That Divide a Number
LeetCode ID: 2520
Pattern: Math / Number Manipulation
Difficulty: Easy
Time Complexity: O(d)   (d = number of digits)
Space Complexity: O(1)

Approach:
1. Store the original number in num.
2. Traverse each digit using a temporary variable:
   - Extract last digit using modulo 10.
   - If digit divides num exactly, increment count.
3. Remove last digit using integer division.
4. Return total valid digits count.
"""

class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        ans = 0

        while temp > 0:
            digit = temp % 10

            if num % digit == 0:
                ans += 1

            temp //= 10

        return ans