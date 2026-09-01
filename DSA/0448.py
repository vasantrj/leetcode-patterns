"""
Problem: Find All Numbers Disappeared in an Array
LeetCode ID: 448
Pattern: Arrays / In-Place Marking
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
(excluding the output list)

Approach:
1. Each number in nums is between 1 and n.
2. Use each number as an index and add n to the
   corresponding position.
3. The modulo operation retrieves the original value
   even after positions have been modified.
4. After marking, any index whose value is still <= n
   corresponds to a missing number.
5. Return all such indices + 1.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(
        self,
        nums: List[int]
    ) -> List[int]:

        n = len(nums)

        for number in nums:

            index = (number - 1) % n

            nums[index] += n

        return [
            index + 1
            for index in range(n)
            if nums[index] <= n
        ]