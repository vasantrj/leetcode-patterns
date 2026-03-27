"""
Problem: Container With Most Water
LeetCode ID: 11
Pattern: Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - left at the beginning
   - right at the end
2. Calculate the area formed by the two lines:
   area = min(height[left], height[right]) * (right - left)
3. Track the maximum area found.
4. Move the pointer with the smaller height inward:
   - because moving the taller one cannot increase area
5. Continue until left < right.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water