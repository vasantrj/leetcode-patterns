"""
Problem: Smallest Stable Index I
LeetCode ID: 3903
Pattern: Arrays / Prefix Maximum / Suffix Minimum
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Compute a suffix minimum array where suffix_min[i] stores the
   minimum value from nums[i] to the end of the array.
2. Traverse the array from left to right while maintaining the
   maximum value seen so far using prefix_max.
3. For each index i:
   - prefix_max represents the maximum value in nums[0..i].
   - suffix_min[i] represents the minimum value in nums[i..n-1].
   - The difference between these values determines whether index i
     is stable.
4. If prefix_max - suffix_min[i] <= k, return i because we are looking
   for the smallest stable index.
5. If no stable index is found, return -1.
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        prefix_max = float("-inf")
        for i, value in enumerate(nums):
            prefix_max = max(prefix_max, value)
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1