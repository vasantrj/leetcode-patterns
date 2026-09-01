"""
Problem: Kids With the Greatest Number of Candies
LeetCode ID: 1431
Pattern: Arrays
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Find the maximum number of candies currently owned
   by any child.
2. For each child, check whether giving all the
   extraCandies makes their total at least equal to
   the current maximum.
3. Return a list of boolean values indicating whether
   each child can have the greatest number of candies.
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
        