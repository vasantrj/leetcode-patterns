"""
Problem: Maximize Active Section with Trade I
LeetCode ID: 3499
Pattern: Greedy / Strings
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Pad the string with '1' at both ends to simplify edge cases.
2. Compress the string into consecutive blocks of identical characters.
3. Count the initial number of active ('1') sections.
4. For every block of '1's, consider trading it:
      - Removing this block merges the adjacent '0' blocks.
      - The gain equals the sizes of the left and right '0' blocks.
5. Track the maximum possible number of active sections.
"""

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        baseline = s.count('1')
        ans = baseline

        for idx in range(1, len(blocks) - 1):
            c, l = blocks[idx]
            if c == '1':
                left = blocks[idx - 1][1]
                right = blocks[idx + 1][1]
                ans = max(ans, baseline + left + right)

        return ans
    