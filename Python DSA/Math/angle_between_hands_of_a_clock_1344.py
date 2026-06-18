"""
Problem: Angle Between Hands of a Clock
LeetCode ID: 1344
Pattern: Math / Geometry
Difficulty: Medium

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Compute the position of the hour hand:
      hour_angle = 30 * hour + 0.5 * minutes
2. Compute the position of the minute hand:
      minute_angle = 6 * minutes
3. Find the absolute difference between the two angles.
4. Return the smaller angle:
      min(diff, 360 - diff)
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
    