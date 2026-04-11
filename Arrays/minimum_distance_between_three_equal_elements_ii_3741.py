"""
Problem: Minimum Distance Between Three Equal Elements II
LeetCode ID: 3741
Pattern: Arrays / Hashing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Store indices of each number using a hashmap.
2. For each value with at least 3 occurrences:
   - Consider consecutive triples (i, j, k).
3. Distance formula:
   (j - i) + (k - j) + (k - i) = 2 * (k - i)
4. So we only need to minimize (k - i).
5. Return the minimum distance, or -1 if no valid triple exists.
"""

from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        for i, x in enumerate(nums):
            indices[x].append(i)

        ans = float('inf')

        for idx_list in indices.values():
            if len(idx_list) >= 3:
                for i in range(len(idx_list) - 2):
                    dist = 2 * (idx_list[i + 2] - idx_list[i])
                    ans = min(ans, dist)

        return ans if ans != float('inf') else -1