"""
Problem: Find the Highest Altitude
LeetCode ID: 1732
Pattern: Prefix Sum
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The biker starts at altitude 0.
2. Traverse the gain array and maintain the current altitude.
3. Track the maximum altitude reached so far.
4. Return the highest altitude encountered.
"""

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest
    
    