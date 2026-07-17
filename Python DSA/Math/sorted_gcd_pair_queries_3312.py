"""
Problem: Sorted GCD Pair Queries
LeetCode ID: 3312
Pattern: Mathematics / Number Theory
Difficulty: Hard

Time Complexity: O(M log M + Q log M)
Space Complexity: O(M)

where:
    M = maximum value in nums
    Q = number of queries

Approach:
1. Count the frequency of every number in nums.
2. For each divisor d, count how many numbers are
   divisible by d.
3. Compute the number of pairs having GCD exactly d
   using inclusion-exclusion:
      - Total pairs divisible by d:
            C(count[d], 2)
      - Subtract pairs already counted for multiples
        of d.
4. Build a prefix sum where prefix[d] stores the
   number of pairs whose GCD is at most d.
5. For each query, use binary search on the prefix
   array to find the corresponding GCD value.
"""

from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxV = max(nums)
        
        freq = [0] * (maxV + 1)
        for x in nums:
            freq[x] += 1
        
        cnt = [0] * (maxV + 1)
        for d in range(1, maxV + 1):
            s = 0
            for m in range(d, maxV + 1, d):
                s += freq[m]
            cnt[d] = s
        
        exact = [0] * (maxV + 1)
        for d in range(maxV, 0, -1):
            total = cnt[d] * (cnt[d] - 1) // 2
            m = 2 * d
            while m <= maxV:
                total -= exact[m]
                m += d
            exact[d] = total
        
        prefix = [0] * (maxV + 1)
        for d in range(1, maxV + 1):
            prefix[d] = prefix[d - 1] + exact[d]
        
        res = []
        for q in queries:
            d = bisect.bisect_right(prefix, q)
            res.append(d)
        
        return res

        