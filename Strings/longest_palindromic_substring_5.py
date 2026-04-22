"""
Problem: Longest Palindromic Substring
LeetCode ID: 5
Pattern: Strings / Expand Around Center
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(1)

Approach:
1. A palindrome mirrors around its center.
2. For every index i, check two centers:
   - Odd length palindrome centered at i      (e.g. "aba")
   - Even length palindrome centered at i,i+1 (e.g. "abba")
3. Expand outward while characters match.
4. Track the longest valid palindrome boundaries.
5. Return the longest substring found.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def expand(l: int, r: int) -> tuple:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1

        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expand(i, i)

            # Even length palindrome
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]