"""
Problem: First Unique Character in a String
LeetCode ID: 387
Pattern: Hash Map / Counting
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the frequency of every character.
2. Traverse the string from left to right.
3. Return the index of the first character whose frequency is 1.
4. If no unique character exists, return -1.
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1