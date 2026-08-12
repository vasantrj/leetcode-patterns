"""
Problem: Length of Longest Subarray With at Most K Frequency
LeetCode ID: 2958
Pattern: Sliding Window / Hash Map
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a sliding window with two pointers, left and right.
2. Maintain the frequency of each number inside the window.
3. Expand the window by moving right.
4. If the frequency of the newly added number exceeds k,
   move left forward until the window becomes valid again.
5. Track the maximum valid window length.
"""

from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        best = 0
        for right, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            while freq[num] > k:
                left_num = nums[left]
                freq[left_num] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

    