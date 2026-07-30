"""
Problem: Largest Perimeter Triangle
LeetCode ID: 976
Pattern: Greedy / Sorting
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort the side lengths in descending order.
2. Check every consecutive triplet.
3. A valid triangle exists if:
      b + c > a
   where a is the largest side.
4. Since the array is sorted in descending order,
   the first valid triangle found has the maximum perimeter.
5. If no valid triangle exists, return 0.
"""

from typing import List

class Solution:
    def largestPerimeter(self,nums: List[int]) -> int:
        nums.sort(reverse=True)
        for index in range(len(nums) - 2):
            largest = nums[index]
            second = nums[index + 1]
            third = nums[index + 2]
            if second + third > largest:
                return largest + second + third
        return 0
    