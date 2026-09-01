"""
Problem: 4Sum II
LeetCode ID: 454
Pattern: Hashing
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Approach:
1. Split the problem into two parts:
   - Compute all possible sums of nums1 and nums2 → store in hashmap.
2. For every sum of nums3 and nums4:
   - Check if -(sum) exists in hashmap.
3. If yes, add its frequency to the result.
4. This reduces O(n^4) brute force to O(n^2).
"""

from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        # Step 1: Store sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                sum_map[s] = sum_map.get(s, 0) + 1
        # Step 2: Find complementary sums from nums3 and nums4
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
        return count