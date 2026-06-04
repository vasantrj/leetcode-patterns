"""
Problem: Intersection of Two Arrays
LeetCode ID: 349
Pattern: Arrays / Hash Set
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(n + m)

Approach:
1. Convert nums1 into a set for O(1) lookups.
2. Traverse nums2:
   - If number exists in set1, add it to result set.
3. Using a set automatically removes duplicates.
4. Convert result set to list and return.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)