"""
Problem: Maximum Average Subarray I
LeetCode ID: 643
Pattern: Sliding Window
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Calculate the sum of the first k elements.
2. Treat those k elements as the initial sliding window.
3. Move the window one position at a time:
      - Add the new element.
      - Remove the element leaving the window.
4. Keep track of the maximum window sum.
5. Divide the maximum sum by k to obtain the maximum average.
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
