"""
Problem: Perfect Number
LeetCode ID: 507
Pattern: Number Theory / Divisors
Difficulty: Easy
Time Complexity: O(sqrt(n))
Space Complexity: O(1)

Approach:
1. A perfect number is a positive integer equal to the sum of its
   positive divisors excluding itself.
2. Numbers less than or equal to 1 cannot be perfect numbers, so
   return False.
3. Initialize total with 1 because 1 is a proper divisor of every
   number greater than 1.
4. Iterate from 2 up to sqrt(num):
   - If i divides num, add i to the divisor sum.
   - Also add num // i, which is the corresponding divisor pair.
   - Avoid adding the same divisor twice when i == num // i.
5. Return True if the sum of all proper divisors equals num.
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                total += divisor
                if divisor != num // divisor:
                    total += num // divisor
            divisor += 1
        return total == num