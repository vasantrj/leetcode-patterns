"""
Problem: Rotate String
LeetCode ID: 796
Pattern: Strings
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If lengths differ, return False.
2. Concatenate string with itself: s + s.
3. If goal is a substring of (s + s), it is a valid rotation.
4. Return result.
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
    