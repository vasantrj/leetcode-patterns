"""
Problem: Merge Strings Alternately
LeetCode ID: 1768
Pattern: Strings / Two Pointers
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

where:
    n = length of word1
    m = length of word2

Approach:
1. Traverse both strings simultaneously using two pointers.
2. Alternately append one character from each string.
3. Once one string is exhausted, append the remaining
   characters of the other string.
4. Join the collected characters to form the final string.
"""

from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        while i < n1 and j < n2:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        result.append(word1[i:])
        result.append(word2[j:])
        return ''.join(result)
        