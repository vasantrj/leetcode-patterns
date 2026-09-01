"""
Problem: Find the Largest Almost Missing Integer
LeetCode ID: 3471
Pattern: Sliding Window / Hash Map
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Handle the special cases k == n and k == 1 directly.
2. For the general case, only the first and last elements
   can potentially appear in exactly one subarray of length k.
3. Count how many length-k windows contain each candidate.
4. If a candidate appears in at most one window, it is
   almost missing.
5. Return the largest valid candidate, or -1 if none exists.
"""

from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            cnt = Counter(nums)
            candidates = [x for x in nums if cnt[x] == 1]
            return max(candidates) if candidates else -1
        def windows_containing(x: int) -> int:
            occ = 0
            c = 0
            for i in range(n):
                if nums[i] == x:
                    occ += 1
                if i >= k:
                    if nums[i - k] == x:
                        occ -= 1
                if i >= k - 1:
                    if occ > 0:
                        c += 1
                        if c > 1:
                            return c
            return c
        ans = -1
        for x in {nums[0], nums[-1]}:
            if windows_containing(x) <= 1:
                ans = max(ans, x)
        return ans
        