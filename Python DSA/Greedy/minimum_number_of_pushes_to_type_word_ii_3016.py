"""
Problem: Minimum Number of Pushes to Type Word II
LeetCode ID: 3016
Pattern: Greedy / Frequency Counting
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the frequency of each lowercase letter.
2. Sort the frequencies in descending order.
3. Assign the most frequent characters to the lowest
   button press cost.
4. Every group of 8 characters requires one additional
   button press.
5. Multiply each frequency by its assigned push cost
   and accumulate the total.
"""

from typing import List
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        freq.sort(reverse=True)
        total = 0
        for i, f in enumerate(freq):
            if f == 0:
                break
            total += f * (i // 8 + 1)
        return total
    