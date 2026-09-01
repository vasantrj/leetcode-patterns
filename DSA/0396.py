"""
Problem: Rotate Function
LeetCode ID: 396
Pattern: Arrays / Math / Prefix Optimization
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Define rotation function:
   F(k) = sum(i * nums[(i+k) % n])
2. Compute:
   - total_sum = sum(nums)
   - F(0) directly
3. Use recurrence:
   F(k) = F(k-1) + total_sum - n * nums[n - k]
4. Iterate k from 1 to n-1 and track maximum.
5. Return maximum value.
"""

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # Compute F(0)
        F = sum(i * num for i, num in enumerate(nums))
        max_val = F

        # Compute F(1) to F(n-1)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)

        return max_val

        