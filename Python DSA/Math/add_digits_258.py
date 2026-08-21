"""
Problem: Add Digits
LeetCode ID: 258
Pattern: Mathematics / Digit Manipulation
Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Continue while the number has more than one digit.
2. Extract each digit using modulo 10.
3. Add all digits together.
4. Replace the number with the calculated digit sum.
5. Repeat until only one digit remains.
"""

class Solution:
    def addDigits(self,num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num