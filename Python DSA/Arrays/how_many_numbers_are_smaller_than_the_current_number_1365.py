"""
Problem: How Many Numbers Are Smaller Than the Current Number
LeetCode ID: 1365
Pattern: Arrays / Brute Force
Difficulty: Easy
Time Complexity: O(n^2)
Space Complexity: O(1) extra (excluding output)

Approach:
1. For each number in nums:
   - Compare it with every other number.
2. Count how many numbers are strictly smaller.
3. Append the count to the result list.
4. Return the final answer list.
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            count = 0

            for j in nums:
                if j < i:
                    count += 1

            ans.append(count)

        return ans