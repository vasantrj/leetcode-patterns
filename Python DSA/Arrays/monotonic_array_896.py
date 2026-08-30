"""
Problem: Monotonic Array
LeetCode ID: 896
Pattern: Arrays
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Assume the array is both increasing and decreasing.
2. Traverse adjacent pairs of elements.
3. If nums[i] > nums[i + 1], the array cannot be increasing.
4. If nums[i] < nums[i + 1], the array cannot be decreasing.
5. The array is monotonic if either possibility remains true.
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False
        return increasing or decreasing