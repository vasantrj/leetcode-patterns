"""
Problem: Repeated Substring Pattern
LeetCode ID: 459
Pattern: Strings / String Matching
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Concatenate the string with itself to form s + s.
2. Remove the first and last characters using (s + s)[1:-1].
3. If s appears in this modified string, then s can be constructed
   by repeating a smaller substring.
4. Return True if s is found; otherwise, return False.
5. This works because a string formed by repeating a substring will
   appear inside the middle portion of its doubled string.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]