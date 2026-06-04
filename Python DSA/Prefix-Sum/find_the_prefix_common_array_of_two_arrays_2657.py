"""
Problem: Find the Prefix Common Array of Two Arrays
LeetCode ID: 2657
Pattern: Prefix Sum / Hashing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Traverse arrays A and B together.
2. Maintain a frequency map/count of seen numbers.
3. For each index i:
   - Mark A[i] and B[i] as seen.
   - Whenever a number becomes seen in both arrays,
     increment common count.
4. Store current common count into answer array.
5. Return final prefix common array.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        common = 0
        ans = []
        for a, b in zip(A, B):
            freq[a] += 1
            if freq[a] == 2:
                common += 1
            freq[b] += 1
            if freq[b] == 2:
                common += 1
            ans.append(common)
        return ans