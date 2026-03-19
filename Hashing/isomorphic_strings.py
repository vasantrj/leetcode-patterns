"""
Problem: Isomorphic Strings
LeetCode ID: 205
Pattern: Hashing
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use two hashmaps:
   - map_st for mapping s → t
   - map_ts for mapping t → s
2. Iterate through both strings together.
3. Check:
   - If mapping already exists but doesn't match → return False
4. Otherwise, store the mapping in both dictionaries.
5. If all mappings are valid → return True
"""

from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        for c1, c2 in zip(s, t):
            if c1 in map_st and map_st[c1] != c2:
                return False
            if c2 in map_ts and map_ts[c2] != c1:
                return False
            map_st[c1] = c2
            map_ts[c2] = c1
        return True