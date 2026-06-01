"""
Problem: Minimum Cost of Buying Candies With Discount
LeetCode ID: 2144
Pattern: Greedy / Sorting
Difficulty: Easy
Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort candies in descending order.
2. For every group of 3 candies:
   - Pay for the two most expensive.
   - Get the third (cheapest) for free.
3. Add costs of candies whose index is not a multiple of 3
   in each sorted group.
4. Return the minimum total cost.
"""

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if i % 3 != 2:  # every 3rd candy is free
                total += cost[i]
        return total
    