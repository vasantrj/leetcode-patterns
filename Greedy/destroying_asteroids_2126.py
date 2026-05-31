"""
Problem: Destroying Asteroids
LeetCode ID: 2126
Pattern: Greedy / Sorting
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Sort asteroids by mass in ascending order.
2. Always destroy the smallest asteroid first.
3. If current mass >= asteroid:
   - Destroy it and add asteroid mass.
4. If current mass < asteroid:
   - We cannot destroy this asteroid or any larger one.
   - Return False.
5. If all asteroids are destroyed, return True.
"""

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True
    