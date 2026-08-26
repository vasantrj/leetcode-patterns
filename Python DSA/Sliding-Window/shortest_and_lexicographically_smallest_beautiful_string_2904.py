"""
Problem: Shortest and Lexicographically Smallest Beautiful String
LeetCode ID: 2904
Pattern: Sliding Window / String
Difficulty: Easy

Time Complexity: O(n²) worst case
Space Complexity: O(n)

Approach:
1. Use a sliding window to maintain at most k ones.
2. Expand the right pointer through the string.
3. When the window contains exactly k ones:
      - Remove leading zeros to get the shortest valid substring
        ending at the current position.
      - Compare it with the current best answer.
4. Prefer:
      - Shorter substring first.
      - Lexicographically smaller substring if lengths are equal.
5. Return the best substring found.
"""

from typing import List

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        left = 0
        ones = 0
        for right in range(n):
            if s[right] == '1':
                ones += 1
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1
            
            if ones == k:
                l = left
                while s[l] == '0':
                    l += 1
                
                candidate = s[l:right + 1]
                if (best == "" 
                        or len(candidate) < len(best) 
                        or (len(candidate) == len(best) and candidate < best)):
                    best = candidate
        
        return best