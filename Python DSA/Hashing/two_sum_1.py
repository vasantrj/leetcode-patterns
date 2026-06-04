"""
Problem: Two Sum
LeetCode ID: 1
Pattern: Hashing / Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. We need to find two indices such that nums[i] + nums[j] == target.
2. Use a hash map to store previously seen numbers and their indices.
3. For each number:
   - Compute the required complement = target - current number.
   - If complement is already in the hash map, return its index and current index.
   - Otherwise, store the current number with its index.
4. This avoids the brute-force O(n^2) approach and gives an O(n) solution.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
