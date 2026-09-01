"""
Problem: Longest Substring of One Repeating Character
LeetCode ID: 2213
Pattern: Segment Tree / String
Difficulty: Hard

Time Complexity: O(n + q log n)
Space Complexity: O(n)

where:
    n = length of the string
    q = number of queries

Approach:
1. Build a segment tree over the string.
2. For every segment, store:
      - leftChar: first character
      - rightChar: last character
      - prefLen: longest repeating prefix
      - sufLen: longest repeating suffix
      - maxLen: longest repeating substring
      - length: segment length
3. When two child segments are merged:
      - Combine their prefixes if their boundary characters match.
      - Combine their suffixes in the same way.
      - Check whether the longest suffix of the left segment
        and longest prefix of the right segment can be joined.
4. For each query, update one character and recalculate
   only the affected segment-tree path.
5. The root always contains the longest repeating substring
   after the current update.
"""

from typing import List

from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        size = 4 * n
        
        leftChar = [''] * size
        rightChar = [''] * size
        prefLen = [0] * size
        sufLen = [0] * size
        maxLen = [0] * size
        length = [0] * size
        
        def pull(node, l, r, mid):
            left = 2 * node
            right = 2 * node + 1
            length[node] = length[left] + length[right]
            leftChar[node] = leftChar[left]
            rightChar[node] = rightChar[right]
            prefLen[node] = prefLen[left]
            if prefLen[left] == length[left] and leftChar[left] == leftChar[right]:
                prefLen[node] += prefLen[right]
            
            sufLen[node] = sufLen[right]
            if sufLen[right] == length[right] and rightChar[right] == rightChar[left]:
                sufLen[node] += sufLen[left]
            
            maxLen[node] = max(maxLen[left], maxLen[right])
            if rightChar[left] == leftChar[right]:
                maxLen[node] = max(maxLen[node], sufLen[left] + prefLen[right])
        
        def build(node, l, r):
            if l == r:
                leftChar[node] = rightChar[node] = s[l]
                prefLen[node] = sufLen[node] = maxLen[node] = length[node] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node, l, r, mid)
        
        def update(node, l, r, idx, ch):
            if l == r:
                leftChar[node] = rightChar[node] = ch
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            pull(node, l, r, mid)
        build(1, 0, n - 1)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            res.append(maxLen[1])
        return res
        