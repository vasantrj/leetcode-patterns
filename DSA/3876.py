"""
Problem: Construct Uniform Parity Array II
LeetCode ID: 3876
Pattern: Hashing / Arrays
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Find the minimum value in the array.
2. If the minimum value is odd, return True (since we can make all elements odd).
3. If the minimum value is even, check if all elements in the array are even.

"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        if mn % 2 == 1:
            return True
        return all(x % 2 == 0 for x in nums1)