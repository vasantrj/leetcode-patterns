"""
Problem: Minimum Number of Pushes to Type Word I
LeetCode ID: 3014
Pattern: Greedy / Hash Map
Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
1. Count the frequency of each character.
2. Sort the frequencies in descending order.
3. Assign the most frequent characters to the cheapest
   button presses.
4. Every group of 8 characters requires one additional
   button press.
5. Multiply each frequency by its assigned push cost and
   accumulate the total.
"""

from collections import Counter


class Solution:
    def minimumPushes(self,word: str) -> int:
        frequencies = sorted(Counter(word).values(),reverse=True)
        total_pushes = 0
        for index, frequency in enumerate(frequencies):
            pushes = (index // 8) + 1
            total_pushes += pushes * frequency
        return total_pushes
    