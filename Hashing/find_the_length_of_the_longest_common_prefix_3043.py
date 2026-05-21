"""
Problem: Find the Length of the Longest Common Prefix
LeetCode ID: 3043
Pattern: Trie / Hash Set
Difficulty: Medium
Time Complexity: O(n * d + m * d)
Space Complexity: O(n * d)

Approach:
1. Convert every prefix of numbers in arr1 into strings.
2. Store all prefixes in a set.
3. For each number in arr2:
   - Generate prefixes incrementally.
   - Check whether prefix exists in the set.
4. Track maximum matching prefix length.
5. Return the maximum length found.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        # Store all prefixes from arr1
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0
        # Check prefixes in arr2
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)
        return ans
    