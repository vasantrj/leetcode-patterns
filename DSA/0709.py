"""
Problem: To Lower Case
LeetCode ID: 709
Pattern: Strings
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use Python's built-in lower() method to convert all uppercase
   characters in the string to lowercase.
2. Characters that are already lowercase or are not alphabetic
   remain unchanged.
3. Return the converted string.
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()