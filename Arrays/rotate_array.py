"""
Problem: Rotate Array
LeetCode ID: 189
Pattern: Array / Reversal Technique
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Normalize k using k = k % n.
2. Reverse the entire array.
3. Reverse the first k elements.
4. Reverse the remaining n-k elements.
This effectively rotates the array to the right by k steps.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: reverse whole array
        reverse(0, n - 1)

        # Step 2: reverse first k elements
        reverse(0, k - 1)

        # Step 3: reverse remaining elements
        reverse(k, n - 1)