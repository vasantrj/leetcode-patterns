"""
Problem: Remove Covered Intervals
LeetCode ID: 1288
Pattern: Greedy / Sorting
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort intervals by:
      - Start point in ascending order.
      - End point in descending order for equal starts.
2. Traverse the sorted intervals while tracking the
   maximum end point seen so far.
3. If the current interval extends beyond max_end,
   it is not covered by any previous interval.
   Count it and update max_end.
4. Otherwise, the current interval is covered and
   can be ignored.
"""

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = 0
        for _, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        
        return count

        