"""
Problem: Jump Game IX
LeetCode ID: 3660
Pattern: Dynamic Programming / Prefix-Suffix
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build prefix maximum array:
   pre_max[i] = maximum value in nums[0..i]
2. Traverse from right to left while maintaining:
   suf_min = minimum value to the right
3. If pre_max[i] > suf_min:
   - We can chain jumps and inherit answer from i+1
4. Otherwise:
   - Best reachable value is pre_max[i]
5. Return final answer array.
"""

from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
        ans = [0] * n
        suf_min = float('inf')
        for i in range(n - 1, -1, -1):
            if pre_max[i] > suf_min and i + 1 < n:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]
            suf_min = min(suf_min, nums[i])
        return ans
    