"""
Problem: Range Sum Query - Immutable
LeetCode ID: 303
Pattern: Prefix Sum
Difficulty: Easy
Time Complexity:
- __init__: O(n)
- sumRange: O(1)

Space Complexity: O(n)

Approach:
1. Build prefix sum array:
   prefix[i] = sum of first i elements
2. Range sum from left to right:
   prefix[right + 1] - prefix[left]
3. This allows O(1) query time.
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

