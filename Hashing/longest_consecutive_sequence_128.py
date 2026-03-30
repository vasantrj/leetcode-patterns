"""
Problem: Longest Consecutive Sequence
LeetCode ID: 128
Pattern: Hashing / Set
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Store all numbers in a set for O(1) lookup.
2. Iterate through the set:
   - Only start counting if (num - 1) is NOT in the set
     → ensures we start from the beginning of a sequence.
3. Expand the sequence using a while loop.
4. Track the maximum length found.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            # Start of sequence
            if num - 1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest