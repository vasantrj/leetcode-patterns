"""
Problem: Unique Number of Occurrences
LeetCode ID: 1207
Pattern: Hash Map / Hash Set / Frequency Counting
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Count the frequency of every number using a hash map.
2. Store all frequencies in a set.
3. If the number of unique frequencies equals the number
   of distinct numbers, every occurrence count is unique.
4. Otherwise, at least two numbers have the same frequency.
"""

from typing import List


class Solution:
    def uniqueOccurrences(
        self,
        arr: List[int]
    ) -> bool:

        count = {}

        # Count the frequency of each number.
        for number in arr:

            count[number] = (
                count.get(number, 0) + 1
            )

        # A set removes duplicate frequencies.
        frequencies = set(count.values())

        return len(frequencies) == len(count)