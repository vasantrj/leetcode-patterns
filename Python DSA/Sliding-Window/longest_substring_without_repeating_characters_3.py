"""
Problem: Longest Substring Without Repeating Characters
LeetCode ID: 3
Pattern: Sliding Window / Hash Set
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(min(n, charset))

Approach:
1. Use two pointers to maintain a window [left, right].
2. Use a set to store characters currently in the window.
3. Expand right pointer one character at a time.
4. If duplicate appears:
   - Shrink window from left until duplicate is removed.
5. Update maximum window length after each valid expansion.
6. Return the maximum length found.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len