"""
Problem: 4Sum
LeetCode ID: 18
Pattern: Two Pointers / Sorting
Difficulty: Medium
Time Complexity: O(n^3)
Space Complexity: O(1) extra (excluding output)

Approach:
1. Sort the array to enable duplicate skipping and two-pointer search.
2. Fix the first number using index i.
3. Fix the second number using index j.
4. Use two pointers:
   - left = j + 1
   - right = n - 1
5. Compare total = nums[i] + nums[j] + nums[left] + nums[right]
   - If equal to target -> store quadruplet
   - If smaller -> move left pointer
   - If larger -> move right pointer
6. Skip duplicates for i, j, left, and right.
7. Return all unique quadruplets.
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
    