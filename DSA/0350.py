"""
Problem: Intersection of Two Arrays II
LeetCode ID: 350
Pattern: Hash Map / Counting
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n)

Approach:
1. Count the frequency of each element in nums1.
2. Traverse nums2.
3. If the current element exists in the frequency map,
   add it to the answer and decrease its count.
4. Return the intersection containing duplicates.
"""

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for n in nums2:
            if counts[n] > 0:
                result.append(n)
                counts[n] -= 1
        
        return result