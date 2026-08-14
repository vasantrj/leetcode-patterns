"""
Problem: Maximum Length Substring With Two Occurrences
LeetCode ID: 3090
Pattern: Sliding Window / Hash Map
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(k)

where:
    n = length of the string
    k = number of distinct characters in the window

Approach:
1. Use a sliding window with left and right pointers.
2. Maintain the frequency of each character inside the window.
3. Expand the window by moving the right pointer.
4. If the current character appears more than twice,
   move the left pointer until the window becomes valid.
5. Track the maximum valid window length.
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len