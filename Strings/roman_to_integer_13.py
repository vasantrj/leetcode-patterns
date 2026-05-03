"""
Problem: Roman to Integer
LeetCode ID: 13
Pattern: Strings / Hashing
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Map Roman symbols to their values.
2. Traverse the string:
   - If current value < next value → subtract it.
   - Otherwise → add it.
3. Sum all values to get final integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
    