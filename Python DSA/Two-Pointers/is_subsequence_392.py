"""
Problem: Is Subsequence
LeetCode ID: 392
Pattern: Two Pointers / Greedy
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use a pointer i to track the current character in s.
2. Traverse t from left to right.
3. Whenever t contains the character s[i], move i forward.
4. If i reaches the length of s, every character of s has
   been matched in order.
5. Return whether all characters of s were matched.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


        