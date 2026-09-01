"""
Problem: Left and Right Sum Differences
LeetCode ID: 2574
Pattern: Prefix Sum
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1) extra space (excluding output)

Approach:
1. Compute the total sum of the array.
2. Maintain a running left_sum.
3. For each element:
   - right_sum = total - left_sum - current element
   - answer = abs(left_sum - right_sum)
4. Update left_sum and continue.
"""

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        ans = []

        for num in nums:
            right_sum = total - left_sum - num
            ans.append(abs(left_sum - right_sum))
            left_sum += num

        return ans