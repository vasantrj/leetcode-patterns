"""
Problem: Minimum Distance Between Three Equal Elements I
LeetCode ID: 3740
Pattern: Arrays / Hashing
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Store indices of each number using a hashmap.
2. For each value with at least 3 occurrences:
   - Check consecutive triples (a, b, c).
3. Compute distance using:
   (b - a) + (c - b) + (c - a)
4. Track the minimum distance.
5. Return -1 if no valid triple exists.
"""

from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)

        result = float('inf')

        for idx_list in indices.values():
            if len(idx_list) >= 3:
                for i in range(len(idx_list) - 2):
                    a, b, c = idx_list[i], idx_list[i + 1], idx_list[i + 2]
                    dist = (b - a) + (c - b) + (c - a)
                    result = min(result, dist)

        return result if result != float('inf') else -1