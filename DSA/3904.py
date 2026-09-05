"""
Problem: Smallest Stable Index II
LeetCode ID: 3904
Pattern: Arrays / Prefix Maximum / Suffix Minimum
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build a prefix maximum array where prefix_max[i] stores the
   maximum value from nums[0] to nums[i].
2. Build a suffix minimum array where suffix_min[i] stores the
   minimum value from nums[i] to nums[n - 1].
3. Traverse every index i and compare:
   - prefix_max[i], the maximum value on the left including i.
   - suffix_min[i], the minimum value on the right including i.
4. If prefix_max[i] - suffix_min[i] <= k, index i is stable.
5. Return the first stable index because the problem asks for the
   smallest stable index.
6. If no stable index satisfies the condition, return -1.
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = [0] * n
        prefix_max[0] = nums[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i

        return -1