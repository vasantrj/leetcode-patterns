"""
Problem: Minimum Distance to the Target Element
LeetCode ID: 1848
Pattern: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the array using enumerate.
2. For every index where nums[i] == target:
   - Compute distance = abs(i - start)
3. Return the minimum distance among all such indices.
"""

class Solution(object):
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i, n in enumerate(nums) if n == target)