"""
Problem: Word Pattern
LeetCode ID: 290
Pattern: Hashing
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Split the string s into words.
2. If length of pattern != number of words → return False.
3. Use two hashmaps:
   - map_p_w for pattern → word
   - map_w_p for word → pattern
4. Iterate through pattern and words together:
   - If mapping exists and mismatches → return False
5. Otherwise, store mapping in both directions.
6. If all mappings are valid → return True
"""

from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_p_w = {}
        map_w_p = {}
        for p, w in zip(pattern, words):
            if p in map_p_w and map_p_w[p] != w:
                return False
            if w in map_w_p and map_w_p[w] != p:
                return False
            map_p_w[p] = w
            map_w_p[w] = p
        return True