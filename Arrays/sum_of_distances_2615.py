"""
Problem: Sum of Distances
LeetCode ID: 2615
Pattern: Prefix Sum / Hashing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Group all indices by their value.
2. For each group of indices:
   - Compute contribution from left side using prefix sums.
   - Compute contribution from right side using suffix sums.
3. For an index idx:
   - Left contribution = k * idx - sum(left indices)
   - Right contribution = sum(right indices) - right_count * idx
4. Add both contributions to answer[idx].
5. Return final answer array.
"""

from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # Group indices by value
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        for indices in groups.values():
            m = len(indices)

            # Left contributions
            prefix = 0
            for k, idx in enumerate(indices):
                ans[idx] += k * idx - prefix
                prefix += idx

            # Right contributions
            suffix = 0
            for k in range(m - 1, -1, -1):
                idx = indices[k]
                right_count = m - 1 - k
                ans[idx] += suffix - right_count * idx
                suffix += idx

        return ans