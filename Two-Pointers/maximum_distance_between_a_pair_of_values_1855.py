"""
Problem: Maximum Distance Between a Pair of Values
LeetCode ID: 1855
Pattern: Two Pointers
Difficulty: Medium
Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. Both nums1 and nums2 are sorted in non-increasing order.
2. We need indices (i, j) such that:
   - i <= j
   - nums1[i] <= nums2[j]
3. Use two pointers:
   - i for nums1
   - j for nums2
4. If condition is valid:
   - update answer with (j - i)
   - move j forward to maximize distance
5. Otherwise:
   - move i forward
   - ensure j >= i
6. Return maximum valid distance found.
"""

from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
                if j < i:
                    j = i

        return max_dist