"""
Problem: 3Sum
LeetCode ID: 15
Pattern: Two Pointers
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(1) (excluding output)

Approach:
1. Sort the array.
2. Iterate through each element as the first number.
3. Use two pointers (left and right) to find pairs such that:
   nums[i] + nums[left] + nums[right] = 0
4. Skip duplicates:
   - Skip same 'i' values
   - Skip duplicate left/right values after finding a valid triplet
5. Adjust pointers based on sum:
   - If sum < 0 → move left
   - If sum > 0 → move right
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result