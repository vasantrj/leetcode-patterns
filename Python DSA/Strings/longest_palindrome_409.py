"""
Problem: Longest Palindrome
LeetCode ID: 409
Pattern: Hashing / Strings
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the frequency of each character.
2. Every pair of characters can be used in the palindrome.
3. Add all even counts directly.
4. For odd counts:
   - Use count - 1 characters (largest even part).
   - Keep one odd character for the center if available.
5. Return the maximum palindrome length.
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        for freq in counts.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length
    
