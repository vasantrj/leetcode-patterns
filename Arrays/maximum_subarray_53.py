"""
Problem: Maximum Subarray
LeetCode ID: 53
Pattern: Array / Dynamic Programming (Kadane's Algorithm)
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use Kadane's Algorithm to find the maximum sum of a contiguous subarray.

1. Initialize:
   current_sum = first element
   max_sum = first element

2. Iterate through the array starting from index 1:
   - At each element decide whether to:
     a) Start a new subarray from the current element
     b) Extend the previous subarray

   current_sum = max(num, current_sum + num)

3. Update the global maximum:
   max_sum = max(max_sum, current_sum)

4. Return max_sum.
"""

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum