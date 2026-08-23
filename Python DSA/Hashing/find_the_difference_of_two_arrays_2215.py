"""
Problem: Find the Difference of Two Arrays
LeetCode ID: 2215
Pattern: Hash Set / Set Difference
Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

where:
    n = length of nums1
    m = length of nums2

Approach:
1. Convert both arrays into sets to remove duplicates.
2. Use set difference to find elements that exist only
   in nums1.
3. Use set difference in the opposite direction to find
   elements that exist only in nums2.
4. Convert both results back to lists.
"""

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

