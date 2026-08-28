"""
Problem: Detect Capital
LeetCode ID: 520
Pattern: String / Character Classification
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the number of uppercase letters in the word.
2. A word is correctly capitalized if:
      - All letters are lowercase.
      - All letters are uppercase.
      - Only the first letter is uppercase.
3. Return True if any of these conditions is satisfied.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = sum(1 for c in word if c.isupper())
        
        if upper_count == 0 or upper_count == len(word):
            return True
        if upper_count == 1 and word[0].isupper():
            return True
        return False