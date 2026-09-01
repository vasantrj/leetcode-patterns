"""
Problem: Two Furthest Houses With Different Colors
LeetCode ID: 2078
Pattern: Arrays / Greedy
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. We need the maximum distance |i - j| such that colors[i] != colors[j].
2. The furthest pair must involve either:
   - first house with some different-colored house from the right, or
   - last house with some different-colored house from the left.
3. Check from the right:
   - Find the farthest index where color differs from colors[0].
4. Check from the left:
   - Find the earliest index where color differs from colors[n-1].
5. Return the maximum of both distances.
"""

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0

        # Compare with first house
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                result = max(result, i)
                break

        # Compare with last house
        for i in range(n - 1):
            if colors[i] != colors[-1]:
                result = max(result, n - 1 - i)
                break

        return result
    