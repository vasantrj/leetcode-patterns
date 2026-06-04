"""
Problem: Valid Palindrome
LeetCode ID: 125
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers: left (start) and right (end).
2. Ignore non-alphanumeric characters using isalnum().
3. Convert characters to lowercase for case-insensitive comparison.
4. If characters mismatch → return False.
5. Move pointers inward until they meet.
6. If all checks pass → return True.
"""

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True