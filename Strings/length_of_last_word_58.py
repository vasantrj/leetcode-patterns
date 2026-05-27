"""
Problem: Length of Last Word
LeetCode ID: 58
Pattern: Strings
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Remove trailing spaces using rstrip().
2. Split the string into words.
3. Return length of the last word.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])