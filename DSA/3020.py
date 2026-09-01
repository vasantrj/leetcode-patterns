"""
Problem: Find the Maximum Number of Elements in Subset
LeetCode ID: 3020
Pattern: Hash Map / Greedy
Difficulty: Medium

Time Complexity: O(n · log log M)
Space Complexity: O(n)

where:
    M = maximum value in nums

Approach:
1. Count the frequency of every number using a hash map.
2. For each unique starting value x:
      - If x == 1:
          • Since 1² = 1, the chain never grows.
          • Use the largest odd number of 1s available.
      - Otherwise:
          • Repeatedly square the current value.
          • If it appears at least twice, use a pair and continue.
          • If it appears once, use it as the center and stop.
          • If it does not exist, remove one element from the
            outermost pair to keep the subset length odd.
3. Return the maximum valid subset length found.
"""


from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1
        
        for x in count:
            if x == 1:
                c = count[1]
                ans = max(ans, c if c % 2 == 1 else c - 1)
                continue
            
            length = 0
            cur = x
            found_center = False
            
            while cur in count:
                if count[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    found_center = True
                    break
            
            if not found_center:
                if length > 0:
                    length -= 1
            
            ans = max(ans, length)
        
        return ans