"""
Problem: Earliest Finish Time for Land and Water Rides II
LeetCode ID: 3635
Pattern: Greedy
Difficulty: Medium

Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. There are only two valid orders:
   - Land → Water
   - Water → Land
2. For a fixed order:
   - Find the earliest finish time of any first ride.
   - Let this be min_end.
3. For every second ride:
   - Start at max(start_time, min_end)
   - Finish at max(start_time, min_end) + duration
4. Take the minimum finish time among all second rides.
5. Compute both orders and return the minimum result.

Key Insight:
For a fixed ordering, finishing the first ride as early as possible
can never hurt. Therefore, we only need the single best first ride
instead of checking every pair.
"""

from typing import List


class Solution:
    def earliestFinishTime(self,landStartTime: List[int],landDuration: List[int],waterStartTime: List[int],waterDuration: List[int]) -> int:
        def calc(firstStart, firstDur, secondStart, secondDur):
            min_end = min(
                start + duration
                for start, duration in zip(firstStart, firstDur)
            )

            return min(
                max(start, min_end) + duration
                for start, duration in zip(secondStart, secondDur)
            )

        return min(
            calc(landStartTime,landDuration,waterStartTime,waterDuration),
            calc(waterStartTime,waterDuration,landStartTime,landDuration)
        )
    