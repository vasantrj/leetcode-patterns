"""
Problem: Minimum Common Value
LeetCode ID: 2540
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - i for nums1
   - j for nums2
2. Compare current values:
   - If equal → return value
   - Smaller value pointer moves forward
3. Continue until one array ends.
4. If no common value exists, return -1.
"""

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1