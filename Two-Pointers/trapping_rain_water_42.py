"""
Problem: Trapping Rain Water
LeetCode ID: 42
Pattern: Two Pointers
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers: left and right.
2. Maintain two variables:
   - left_max → max height from left
   - right_max → max height from right
3. If height[left] < height[right]:
   - If height[left] >= left_max → update left_max
   - Else → water += left_max - height[left]
   - Move left pointer
4. Else:
   - If height[right] >= right_max → update right_max
   - Else → water += right_max - height[right]
   - Move right pointer
5. Continue until left < right.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water