"""
Problem: Degree of an Array
LeetCode ID: 697
Pattern: Hash Map / Frequency Counting
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Track the first occurrence, last occurrence, and
   frequency of every number.
2. Find the degree of the array, which is the maximum
   frequency of any number.
3. For every number having the maximum frequency, calculate
   the length of its smallest subarray containing all of
   its occurrences.
4. Return the minimum of these lengths.
"""

from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        
        result = len(nums)
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                result = min(result, length)
        
        return result
        