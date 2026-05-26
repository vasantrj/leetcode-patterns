"""
Problem: Find the Index of the First Occurrence in a String
LeetCode ID: 28
Pattern: Strings / Sliding Window
Difficulty: Easy
Time Complexity: O((n-m+1) * m)
Space Complexity: O(1)

Approach:
1. Traverse all possible starting positions in haystack.
2. For each position:
   - Compare substring with needle.
3. If match found:
   - return starting index.
4. If no match exists:
   - return -1.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
    