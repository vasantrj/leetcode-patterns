"""
Problem: Words Within Two Edits of Dictionary
LeetCode ID: 2452
Pattern: Strings / Brute Force
Difficulty: Medium
Time Complexity: O(q * d * L)
Space Complexity: O(1) extra (excluding output)

Approach:
1. For each query word:
   - Compare it with every dictionary word.
2. Count character mismatches at corresponding positions.
3. If mismatches <= 2 for any dictionary word:
   - Add query to result.
4. Return all valid query words in original order.
"""

from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def within_two_edits(word: str, target: str) -> bool:
            diff = sum(a != b for a, b in zip(word, target))
            return diff <= 2

        result = []

        for query in queries:
            if any(within_two_edits(query, word) for word in dictionary):
                result.append(query)

        return result