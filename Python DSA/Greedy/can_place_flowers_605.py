"""
Problem: Can Place Flowers
LeetCode ID: 605
Pattern: Greedy
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the flowerbed from left to right.
2. For every empty plot:
      - Check if both adjacent plots are empty (or out of bounds).
3. If a flower can be planted:
      - Plant it immediately (greedy choice).
      - Increment the planted flower count.
4. Return True if at least n flowers can be planted;
   otherwise, return False.
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == m - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n