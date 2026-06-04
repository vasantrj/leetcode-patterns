"""
Problem: 3Sum Closest
LeetCode ID: 16
Pattern: Two Pointers
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(1)

Approach:
1. Sort the array.
2. Iterate through each element as the first number.
3. Use two pointers (left and right) to find the triplet sum closest to target.
4. Track the closest sum found so far.
5. If current sum is closer to target, update closest.
6. Move pointers:
   - If total < target → move left
   - If total > target → move right
   - If total == target → return immediately (best possible answer)
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest