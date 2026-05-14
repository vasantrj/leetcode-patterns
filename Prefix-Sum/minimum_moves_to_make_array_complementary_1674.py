"""
Problem: Minimum Moves to Make Array Complementary
LeetCode ID: 1674
Pattern: Prefix Sum / Sweep Line
Difficulty: Medium
Time Complexity: O(n + limit)
Space Complexity: O(limit)

Approach:
1. Pair elements:
   nums[i] with nums[n-1-i]
2. For each pair:
   - Current sum = a + b
   - Minimum possible sum with 1 move:
       min(a, b) + 1
   - Maximum possible sum with 1 move:
       max(a, b) + limit
3. Use difference array to track move costs efficiently.
4. Initially every sum requires 2 moves.
5. Update ranges:
   - 1 move range
   - 0 move exact sum
6. Prefix sum over diff array gives moves for each target sum.
7. Return minimum moves.
"""

from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            total = a + b

            # Default = 2 moves
            diff[2] += 2

            # One move range
            diff[low] -= 1
            diff[high + 1] += 1

            # Zero move exact sum
            diff[total] -= 1
            diff[total + 1] += 1
            
        ans = float('inf')
        curr = 0
        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)

        return ans