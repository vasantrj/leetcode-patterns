"""
Problem: Summary Ranges
LeetCode ID: 228
Pattern: Arrays / Two Pointers
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
(excluding the output list)

Approach:
1. Traverse the array using an index.
2. Mark the beginning of the current range.
3. Continue while consecutive numbers differ by 1.
4. If the range has one element, add that number.
5. Otherwise, add it in "start->end" format.
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        i = 0
        
        while i < n:
            start = i
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == i:
                result.append(str(nums[start]))
            else:
                result.append(f"{nums[start]}->{nums[i]}")
            i += 1
        
        return result