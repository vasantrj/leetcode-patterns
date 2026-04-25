"""
Problem: Palindrome Number
LeetCode ID: 9
Pattern: Math / Number Manipulation
Difficulty: Easy
Time Complexity: O(log10(n))
Space Complexity: O(1)

Approach:
1. Negative numbers are never palindromes.
2. Numbers ending in 0 (except 0 itself) cannot be palindromes.
3. Reverse only half of the digits:
   - Build reversed_half until it becomes >= remaining x.
4. Compare:
   - Even length: x == reversed_half
   - Odd length:  x == reversed_half // 10
5. This avoids reversing the full number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10