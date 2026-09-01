"""
Problem: Count Odd Numbers in an Interval Range
LeetCode ID: 1523
Pattern: Math
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Count odd numbers from 0 to high:
   (high + 1) // 2
2. Count odd numbers from 0 to low - 1:
   low // 2
3. Subtract both counts to get odds in [low, high].
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)