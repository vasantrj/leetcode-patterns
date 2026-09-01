"""
Problem: Happy Number
LeetCode ID: 202
Pattern: Math / Hash Set
Difficulty: Easy
Time Complexity: O(log n) per iteration
Space Complexity: O(log n)

Approach:
1. Repeatedly replace n with the sum of squares of its digits.
2. If n becomes 1, it is a happy number.
3. If a number repeats, a cycle exists, so it is not happy.
4. Use a set to track previously seen values.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True