"""
Problem: Minimum Absolute Distance Between Mirror Pairs
LeetCode ID: 3761
Pattern: Arrays / Hashing
Difficulty: Medium
Time Complexity: O(n * d)  (d = number of digits)
Space Complexity: O(n)

Approach:
1. Define a helper function to reverse digits of a number.
2. Traverse the array:
   - If current value already exists in hashmap, update answer.
   - Store the reversed value in hashmap with current index.
3. This ensures we match numbers with their mirror counterparts.
4. Return minimum distance, else -1.
"""

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            return int(str(x)[::-1])

        pos = {}
        ans = float('inf')

        for i, v in enumerate(nums):
            if v in pos:
                ans = min(ans, i - pos[v])

            pos[rev(v)] = i

        return ans if ans != float('inf') else -1