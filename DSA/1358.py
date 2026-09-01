"""
Problem: Number of Substrings Containing All Three Characters
LeetCode ID: 1358
Pattern: Sliding Window / Two Pointers
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain a sliding window [left, right] and the
   frequency of 'a', 'b', and 'c' inside it.
2. Expand the window by moving right one step at a time.
3. While the current window contains all three characters,
   shrink it from the left to find the smallest valid window.
4. After shrinking, every starting index before left forms
   a valid substring ending at right.
5. Add left to the answer for each right position.
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        res = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[left]] -= 1
                left += 1
            res += left
        return res

        