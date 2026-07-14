"""
Problem: Find the Number of Subsequences With Equal GCD
LeetCode ID: 3336
Pattern: Dynamic Programming / GCD DP
Difficulty: Hard

Time Complexity: O(n × S)

Space Complexity: O(S)

where:
    n = length of nums
    S = number of distinct (gcd1, gcd2) states

Approach:
1. Use dynamic programming where each state stores:
      (gcd of first subsequence, gcd of second subsequence).
2. Initially, both subsequences are empty:
      dp[(0, 0)] = 1
3. For every number, consider three choices:
      - Skip the number.
      - Add it to the first subsequence.
      - Add it to the second subsequence.
4. Update the corresponding GCD values using the gcd()
   function.
5. After processing all numbers, sum the counts of
   states where both subsequences have the same
   non-zero GCD.
"""

from collections import defaultdict
from typing import List
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        for num in nums:
            new_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD
                
                ng1 = num if g1 == 0 else math.gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD
                
                ng2 = num if g2 == 0 else math.gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD
            
            dp = new_dp
        
        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + cnt) % MOD
        
        return ans
        