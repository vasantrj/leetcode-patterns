"""
Problem: Sort Characters By Frequency
LeetCode ID: 451
Pattern: Hashing / Bucket Sort
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Count frequency of each character using a hashmap.
2. Create buckets where index = frequency.
3. Place characters into corresponding buckets.
4. Traverse buckets from highest frequency to lowest.
5. Build result string by repeating characters based on frequency.
"""

from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Frequency map
        freq_map = {}
        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1
        # Step 2: Buckets
        n = len(s)
        buckets = [[] for _ in range(n + 1)]
        for ch, freq in freq_map.items():
            buckets[freq].append(ch)
        # Step 3: Build result
        result = []
        for i in range(n, 0, -1):
            for ch in buckets[i]:
                result.append(ch * i)
        return "".join(result)