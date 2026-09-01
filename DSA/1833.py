"""
Problem: Maximum Ice Cream Bars
LeetCode ID: 1833
Pattern: Greedy / Sorting
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort the ice cream costs in ascending order.
2. Always buy the cheapest ice cream first.
3. Continue purchasing while enough coins remain.
4. Count how many ice creams can be bought.

Why Greedy Works:
Buying a more expensive ice cream before a cheaper one
can only reduce the total number of ice creams purchased.
Therefore, choosing the cheapest available ice cream first
always maximizes the count.
"""

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if cost > coins:
                break
            coins -= cost
            count += 1
        return count
    