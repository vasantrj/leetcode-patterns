"""
Problem: Rank Transform of an Array
LeetCode ID: 1331
Pattern: Arrays / Hash Map
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Remove duplicate values using a set.
2. Sort the unique values in ascending order.
3. Assign ranks starting from 1 to each unique value.
4. Replace every element in the original array with
   its corresponding rank.
"""

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[v] for v in arr]
        