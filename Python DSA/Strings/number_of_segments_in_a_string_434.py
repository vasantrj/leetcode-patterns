"""
Problem: Number of Segments in a String
LeetCode ID: 434
Pattern: String / Traversal
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the string character by character.
2. A new segment starts when:
      - The current character is not a space.
      - The previous character is either a space or does not exist.
3. Count every such starting position.
"""


class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        return count