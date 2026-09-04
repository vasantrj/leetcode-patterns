"""
Problem: Keyboard Row
LeetCode ID: 500
Pattern: Arrays / Sets / Hashing
Difficulty: Easy
Time Complexity: O(n * m)
Space Complexity: O(m)

Approach:
1. Create a set for each of the three keyboard rows.
2. Traverse each word in the input list.
3. Convert the word to lowercase and create a set of its characters.
4. Check whether all characters of the word belong to any one
   keyboard row:
   - If the character set is a subset of a row, the word can be
     typed using only that row.
   - If it matches any row, add the original word to the result.
5. Return the list of words that can be typed using a single row.
"""

from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"),]
        result = []
        for word in words:
            characters = set(word.lower())
            if any(characters <= row for row in rows):
                result.append(word)
        return result