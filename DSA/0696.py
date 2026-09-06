"""
Problem: Count Binary Substrings
LeetCode ID: 696
Pattern: Strings / Grouping / Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Group consecutive identical characters in the binary string and
   store the size of each group.
2. For every two adjacent groups:
   - A valid binary substring can be formed using equal numbers of
     characters from the two groups.
   - Therefore, the number of valid substrings between two groups is
     min(groups[i], groups[i + 1]).
3. Sum the minimum sizes of all adjacent groups to get the total
   number of valid binary substrings.
4. Return the total count.
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1

        groups.append(count)
        return sum(
            min(groups[i], groups[i + 1])
            for i in range(len(groups) - 1)
        )