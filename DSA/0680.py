"""
Problem: Valid Palindrome II
LeetCode ID: 680
Pattern: Two Pointers / Greedy
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers from both ends of the string.
2. Continue while the characters match.
3. At the first mismatch, we are allowed to remove
   at most one character.
4. Try both possibilities:
      - Remove the left character.
      - Remove the right character.
5. Check whether either remaining substring is a palindrome.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_pal(i + 1, j) or is_pal(i, j - 1)
            i += 1
            j -= 1
        return True