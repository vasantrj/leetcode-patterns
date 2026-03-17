"""
Problem: Contains Duplicate II
LeetCode ID: 219
Pattern: Hashing / Sliding Window
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a hashmap to store the last index of each number.
2. Traverse the array:
   - If the number is already seen and the index difference is <= k, return True.
3. Update the index of the current number in the hashmap.
4. If no such pair is found, return False.
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True
            seen[num] = i
        return False