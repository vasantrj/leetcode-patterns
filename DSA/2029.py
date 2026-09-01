"""
Problem: Stone Game IX
LeetCode ID: 2029
Pattern: Game Theory / Mathematics / Modular Arithmetic
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Group stones by their remainder modulo 3.
2. Only the remainder matters because the running sum
   determines whether a move is divisible by 3.
3. Let cnt[0], cnt[1], and cnt[2] represent the number
   of stones with each remainder.
4. The parity of cnt[0] determines how the game behaves:
      - If cnt[0] is even, Alice wins when both remainder-1
        and remainder-2 stones are available.
      - If cnt[0] is odd, Alice wins only when the difference
        between cnt[1] and cnt[2] is greater than 2.
"""

from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
        
        if cnt[0] % 2 == 0:
            return cnt[1] >= 1 and cnt[2] >= 1
        else:
            return abs(cnt[1] - cnt[2]) > 2
        