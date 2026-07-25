"""
Problem: Excel Sheet Column Number
LeetCode ID: 171
Pattern: Mathematics / Base Conversion
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the column title from left to right.
2. Treat the title as a base-26 number.
3. For each character:
      - Multiply the current result by 26.
      - Add the character's value ('A' = 1, ..., 'Z' = 26).
4. Return the computed column number.
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result