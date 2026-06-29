"""
Problem: Number of Strings That Appear as Substrings in Word
LeetCode ID: 1967
Pattern: Strings
Difficulty: Easy

Time Complexity: O(n × m)
Space Complexity: O(1)

where:
    n = number of patterns
    m = average pattern length

Approach:
1. Traverse each pattern.
2. Check whether it appears as a substring of the given word.
3. Count every matching pattern.
4. Return the total count.
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
    
    