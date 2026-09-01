"""
Problem: Find Missing Elements
LeetCode ID: 3731
Pattern: Hash Set
Difficulty: Easy

Time Complexity: O(n + r)
Space Complexity: O(n)

where:
    n = number of elements
    r = max(nums) - min(nums)

Approach:
1. Find the minimum and maximum values in the array.
2. Store all numbers in a hash set for O(1) lookups.
3. Traverse every integer between the minimum and maximum.
4. Add numbers that are not present in the set to the result.
5. Return the list of missing elements.
"""

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        present = set(nums)
        return [x for x in range(mn + 1, mx) if x not in present]
        