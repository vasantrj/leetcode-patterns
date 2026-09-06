"""
Problem: License Key Formatting
LeetCode ID: 482
Pattern: Strings / String Manipulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Remove all existing hyphens from the string and convert all
   remaining characters to uppercase.
2. Find the size of the first group:
   - The first group contains n % k characters.
   - If n % k == 0, the first group contains k characters.
3. Add the first group to the result.
4. Starting from the end of the first group, divide the remaining
   characters into groups of size k.
5. Join all groups using hyphens and return the formatted string.
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        first_length = n % k or k
        groups = [s[:first_length]]
        for i in range(first_length, n, k):
            groups.append(s[i:i + k])
        return "-".join(groups)