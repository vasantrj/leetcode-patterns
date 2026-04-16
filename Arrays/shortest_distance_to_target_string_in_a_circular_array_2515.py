"""
Problem: Shortest Distance to Target String in a Circular Array
LeetCode ID: 2515
Pattern: Arrays / Simulation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the array and find all indices where words[i] == target.
2. For each such index:
   - Compute clockwise distance: (i - startIndex) % n
   - Compute counter-clockwise distance: (startIndex - i) % n
3. Take the minimum of these distances.
4. If target does not exist, return -1.
"""

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')

        for i, word in enumerate(words):
            if word == target:
                clockwise = (i - startIndex) % n
                counter = (startIndex - i) % n
                min_dist = min(min_dist, clockwise, counter)

        return -1 if min_dist == float('inf') else min_dist