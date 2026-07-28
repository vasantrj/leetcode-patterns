"""
Problem: Smallest Palindromic Rearrangement I
LeetCode ID: 3517
Pattern: Strings / Greedy / Hash Map
Difficulty: Medium

Time Complexity: O(n + k log k)
Space Complexity: O(n)

where:
    n = length of the string
    k = number of distinct characters

Approach:
1. Count the frequency of each character.
2. Traverse characters in sorted order.
3. Add half of each character to the left half.
4. Store the odd-frequency character as the middle.
5. Construct the palindrome as:
      left_half + middle + reverse(left_half)
6. Since characters are processed in sorted order,
   the resulting palindrome is lexicographically smallest.
"""

from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        mid = ''
        half = []
        for c in sorted(cnt.keys()):
            c_count = cnt[c]
            if c_count % 2 == 1:
                mid = c
            half.append(c * (c_count // 2))
        
        half_str = ''.join(half)
        return half_str + mid + half_str[::-1]