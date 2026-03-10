"""
Problem: Merge Sorted Array
LeetCode ID: 88
Pattern: Two Pointers
Difficulty: Easy
Time Complexity: O(m + n)
Space Complexity: O(1)

Approach:
1. Use three pointers starting from the end of the arrays.
2. i -> last valid element in nums1
   j -> last element in nums2
   k -> last position in nums1 (m + n - 1)
3. Compare nums1[i] and nums2[j] and place the larger one at nums1[k].
4. Move pointers accordingly.
5. Continue until all elements of nums2 are merged.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1