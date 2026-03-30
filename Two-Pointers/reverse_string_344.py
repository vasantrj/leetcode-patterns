"""
Problem: Reverse String
LeetCode ID: 344
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - left at the start
   - right at the end
2. Swap characters at left and right.
3. Move left forward and right backward.
4. Continue until left >= right.
5. Modify the list in-place.
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1