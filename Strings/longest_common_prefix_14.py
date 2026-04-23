"""
Problem: Longest Common Prefix
LeetCode ID: 14
Pattern: Strings
Difficulty: Easy
Time Complexity: O(S)   (S = total characters in all strings)
Space Complexity: O(1)

Approach:
1. If the list is empty, return "".
2. Use zip(*strs) to iterate column-wise across all strings.
3. For each character column:
   - If all characters are same, continue.
   - If mismatch found, return prefix up to previous index.
4. If all columns match, the shortest string itself is the answer.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]

        return min(strs, key=len)
    
    