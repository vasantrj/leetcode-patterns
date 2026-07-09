"""
Problem: Path Existence Queries in a Graph I
LeetCode ID: 3532
Pattern: Graphs / Connected Components
Difficulty: Medium

Time Complexity: O(n + q)
Space Complexity: O(n)

where:
    n = number of nodes
    q = number of queries

Approach:
1. Since nums is sorted, determine connected components
   by scanning consecutive elements.
2. If the difference between consecutive values is at
   most maxDiff, they belong to the same component.
3. Otherwise, start a new component.
4. Store a component ID for every index.
5. For each query, return True if both indices belong
   to the same component; otherwise return False.
"""

from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                group[i] = group[i - 1]
            else:
                group[i] = group[i - 1] + 1
        
        return [group[u] == group[v] for u, v in queries]

        