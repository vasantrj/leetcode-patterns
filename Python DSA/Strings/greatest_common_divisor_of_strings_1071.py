"""
Problem: Greatest Common Divisor of Strings
LeetCode ID: 1071
Pattern: Strings / Mathematics
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(1)

where:
    n = length of str1
    m = length of str2

Approach:
1. Check whether both strings can be formed by repeating
   the same base string.
2. This is true only if:
      str1 + str2 == str2 + str1
3. If not, no common divisor string exists.
4. Otherwise, the length of the greatest common divisor
   string is gcd(len(str1), len(str2)).
5. Return the prefix of that length from either string.
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]

        