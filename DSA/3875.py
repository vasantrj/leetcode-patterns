"""
Problem: Construct Uniform Parity Array I
LeetCode ID: 3875
Pattern: Arrays / Parity
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Count the number of odd elements in the array.
2. A uniform even array is feasible unless there is exactly one odd element.
3. A uniform odd array is feasible whenever there is at least one odd element.
4. Therefore, the only impossible case is when exactly one element is odd.
5. Return whether either uniform parity is achievable.

Key Insight:
The array can be transformed into a uniform parity array unless it
contains exactly one odd element. Therefore, the answer is False only
when the number of odd elements is exactly one.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odd_count = sum(1 for x in nums1 if x % 2 == 1)        
        feasible_even = (odd_count != 1)
        feasible_odd = (odd_count >= 1)
        return feasible_even or feasible_odd
        