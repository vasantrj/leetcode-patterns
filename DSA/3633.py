"""
Problem: Earliest Finish Time for Land and Water Rides I
LeetCode ID: 3633
Pattern: Greedy
Difficulty: Medium
Time Complexity: O(n * m)
Space Complexity: O(1)

Approach:
1. Try both possible orders:
   - Land ride → Water ride
   - Water ride → Land ride
2. For every pair of rides:
   - First ride starts at its available start time.
   - Second ride starts at:
       max(second_start_time, first_finish_time)
3. Compute finish time for all combinations.
4. Return the minimum finish time found.
"""

from typing import List


class Solution:
    def earliestFinishTime(self,landStartTime: List[int],landDuration: List[int],waterStartTime: List[int],waterDuration: List[int]) -> int:
        ans = float("inf")

        # Land -> Water
        for ls, ld in zip(landStartTime, landDuration):
            land_finish = ls + ld

            for ws, wd in zip(waterStartTime, waterDuration):
                finish = max(ws, land_finish) + wd
                ans = min(ans, finish)

        # Water -> Land
        for ws, wd in zip(waterStartTime, waterDuration):
            water_finish = ws + wd

            for ls, ld in zip(landStartTime, landDuration):
                finish = max(ls, water_finish) + ld
                ans = min(ans, finish)

        return ans