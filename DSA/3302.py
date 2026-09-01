"""
Problem: Find the Lexicographically Smallest Valid Sequence
LeetCode ID: 3302
Pattern: Greedy / String Matching
Difficulty: Medium

Time Complexity: O(n + m)
Space Complexity: O(m)

Approach:
1. If word2 is longer than word1, no valid sequence exists.
2. Build a suffix array where suf[j] stores the earliest
   index in word1 from which word2[j:] can be matched.
3. Traverse word1 from left to right.
4. Whenever the current character matches word2[j], take it.
5. At most one character can be changed:
      - If the current character does not match, use the
        change only when the remaining suffix can still
        match word2.
6. Since indices are selected from left to right and the
   earliest possible index is always chosen, the resulting
   sequence is lexicographically smallest.
"""

from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []

        suf = [-1] * (m + 1)
        suf[m] = n
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        result = []
        pos = 0
        jj = 0
        change_used = False

        while jj < m:
            if pos >= n:
                return []
            if word1[pos] == word2[jj]:
                result.append(pos)
                pos += 1
                jj += 1
            elif not change_used and pos + 1 <= suf[jj + 1]:
                result.append(pos)
                pos += 1
                jj += 1
                change_used = True
            else:
                pos += 1

        return result
        