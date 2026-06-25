"""
Problem: Count Subarrays With Majority Element I
LeetCode ID: 3737
Pattern: Arrays / Brute Force
Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(1)

Approach:
1. Iterate over every possible starting index.
2. Extend the subarray one element at a time.
3. Maintain a balance:
      +1 if the current element equals target
      -1 otherwise
4. If the balance becomes positive, the target
   appears more than half the time in the current
   subarray, so count it.
5. Return the total number of valid subarrays.
"""

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for l in range(n):
            balance = 0
            for r in range(l, n):
                balance += 1 if nums[r] == target else -1
                if balance > 0:
                    count += 1

        return count

        