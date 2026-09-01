"""
Problem: Number of ZigZag Arrays I
LeetCode ID: 3699
Pattern: Dynamic Programming
Difficulty: Hard

Time Complexity: O(n × m)
Space Complexity: O(m)

where:
    m = r - l + 1

Approach:
1. Let dp_up[v] represent the number of valid arrays
   ending at value v where the last move was UP.
2. Let dp_down[v] represent the number of valid arrays
   ending at value v where the last move was DOWN.
3. Use prefix sums to efficiently compute transitions:
      new_up[w]   = sum(dp_down[u]) for u < w
      new_down[w] = sum(dp_up[u])   for u > w
4. Iterate through positions and update the DP arrays.
5. The answer is the sum of all valid states modulo 1e9+7.
"""

import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        dp_up = np.arange(m, dtype=np.int64)       
        dp_down = np.arange(m-1, -1, -1, dtype=np.int64) 
        
        for _ in range(2, n):
            pre_up = np.cumsum(dp_up) % MOD      
            pre_down = np.cumsum(dp_down) % MOD  
            
            total_up = pre_up[-1]
            
            new_up = np.empty(m, dtype=np.int64)
            new_up[0] = 0
            new_up[1:] = pre_down[:-1]
            
            new_down = (total_up - pre_up) % MOD
            
            dp_up = new_up % MOD
            dp_down = new_down % MOD
        
        return int((dp_up.sum() + dp_down.sum()) % MOD)

        