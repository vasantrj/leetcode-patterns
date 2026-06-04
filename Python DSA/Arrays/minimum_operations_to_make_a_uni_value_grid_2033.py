"""
Problem: Minimum Operations to Make a Uni-Value Grid
LeetCode ID: 2033
Pattern: Arrays / Math / Median
Difficulty: Medium
Time Complexity: O(m * n log(m * n))
Space Complexity: O(m * n)

Approach:
1. Flatten the grid into a single list.
2. To make all values equal using +/- x:
   - Every value must have the same remainder modulo x.
   - If not, return -1.
3. Sort the flattened list.
4. The optimal target value is the median.
5. Sum operations needed:
   abs(value - median) // x
6. Return total operations.
"""

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [value for row in grid for value in row]

        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations
    