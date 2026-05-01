"""
Problem: Remove Element
LeetCode ID: 27
Pattern: Arrays / Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - write pointer (k) for placing valid elements
   - read pointer (i) to scan array
2. Traverse nums:
   - If nums[i] != val:
       place it at nums[k] and increment k
3. Return k as the new length.
4. Elements beyond k are irrelevant.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k