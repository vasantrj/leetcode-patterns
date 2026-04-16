"""
Problem: Closest Equal Element Queries
LeetCode ID: 3488
Pattern: Arrays / Hashing / Circular Array
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Group indices of equal values using a hashmap.
2. For each group of indices:
   - Treat indices as circular.
   - Compute distance between consecutive indices.
3. Update minimum distance for both endpoints.
4. For each query index:
   - Return precomputed minimum distance or -1 if none exists.
"""

from typing import List
from collections import defaultdict


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        min_dist = [float("inf")] * n

        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        for idxs in positions.values():
            m = len(idxs)
            if m == 1:
                continue

            for i in range(m):
                left = idxs[i]
                right = idxs[(i + 1) % m]

                if right > left:
                    gap = right - left
                else:
                    gap = n - left + right

                min_dist[left] = min(min_dist[left], gap)
                min_dist[right] = min(min_dist[right], gap)

        return [-1 if min_dist[x] == float("inf") else min_dist[x] for x in queries]