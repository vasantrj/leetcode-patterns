"""
Problem: Product of Array Except Self
LeetCode ID: 238
Pattern: Arrays / Prefix-Suffix
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)  # excluding the output array

Approach:
1. Create a result array initialized with 1s.
2. Traverse from left to right and store prefix products in result.
3. Traverse from right to left and multiply suffix products.
4. The result array will contain the product of all elements except itself.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result