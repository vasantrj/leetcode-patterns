"""
Problem: Longest Subsequence With Non-Zero Bitwise XOR
LeetCode ID: 3702
Pattern: Bit Manipulation / XOR / Greedy
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Compute the XOR of all elements.
2. If the total XOR is non-zero, the entire array is a
   valid subsequence.
3. If the total XOR is zero but at least one element is
   non-zero, remove one non-zero element. The resulting
   XOR becomes non-zero, giving a subsequence of length n - 1.
4. If every element is zero, every subsequence has XOR zero,
   so no non-empty valid subsequence exists.
"""

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            total ^= x
        if total != 0:
            return len(nums)
        if any(x != 0 for x in nums):
            return len(nums) - 1
        return 0

        