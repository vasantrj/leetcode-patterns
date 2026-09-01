"""
Problem: Maximum Total Subarray Value I
LeetCode ID: 3689
Pattern: Greedy / Math
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The value of a subarray is:
      max(subarray) - min(subarray)

2. To maximize the value, choose a subarray containing:
      global maximum element
      global minimum element

3. This gives the maximum possible subarray value:
      global_max - global_min

4. Since subarrays can overlap and may be chosen multiple times,
   we can select the same optimal subarray exactly k times.

5. Therefore:
      Answer = k × (global_max - global_min)
"""

from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

        