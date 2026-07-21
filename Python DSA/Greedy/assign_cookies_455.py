"""
Problem: Assign Cookies
LeetCode ID: 455
Pattern: Greedy / Two Pointers
Difficulty: Easy

Time Complexity: O(n log n + m log m)
Space Complexity: O(1)

Approach:
1. Sort both the children's greed factors and the cookie sizes.
2. Use two pointers:
      - One for children.
      - One for cookies.
3. If the current cookie can satisfy the current child,
   assign it and move to the next child.
4. Always move to the next cookie.
5. The number of satisfied children is the answer.
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
    