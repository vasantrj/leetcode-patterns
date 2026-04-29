"""
Problem: Maximum Score From Grid Operations
LeetCode ID: 3225
Pattern: Dynamic Programming / Prefix Sum
Difficulty: Hard
Time Complexity: O(n^3)
Space Complexity: O(n^2)

Approach:
1. Convert each column into prefix sums so we can quickly compute sums of segments.
2. Let dp[h_cur][h_prev] represent:
   - current column height = h_cur
   - previous column height = h_prev
3. While processing column c:
   - we finalize score of column c-1 using heights:
     h_prev (col c-1), h_cur (col c), and h_pp (col c-2)
4. Transition uses optimized prefix and suffix maximums to reduce complexity:
   - Case 1: h_pp <= h_cur
   - Case 2a: h_pp > h_cur and h_pp > h_prev
   - Case 2b: h_pp > h_cur and h_pp <= h_prev
5. After processing all columns, finalize last column separately.
6. Return maximum score.
"""

from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: prefix sums for each column
        pre = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for h in range(1, n + 1):
                pre[c][h] = pre[c][h - 1] + grid[h - 1][c]

        NEG_INF = float('-inf')

        # dp[h_cur][h_prev]
        dp = [[NEG_INF] * (n + 1) for _ in range(n + 1)]
        for h in range(n + 1):
            dp[h][0] = 0

        # Process columns
        for c in range(1, n):
            pc1 = pre[c - 1]

            pmx = [[NEG_INF] * (n + 1) for _ in range(n + 1)]
            smx = [[NEG_INF] * (n + 2) for _ in range(n + 1)]
            smx0 = [[NEG_INF] * (n + 2) for _ in range(n + 1)]

            # Precompute prefix/suffix max
            for hp in range(n + 1):
                dp_hp = dp[hp]

                pmx_hp = pmx[hp]
                smx_hp = smx[hp]
                smx0_hp = smx0[hp]

                pmx_hp[0] = dp_hp[0]
                for k in range(1, n + 1):
                    v = dp_hp[k]
                    pmx_hp[k] = max(pmx_hp[k - 1], v)

                for k in range(n, -1, -1):
                    v = dp_hp[k]
                    val = (v + pc1[k]) if v != NEG_INF else NEG_INF
                    smx_hp[k] = max(val, smx_hp[k + 1])
                    smx0_hp[k] = max(v, smx0_hp[k + 1])

            new_dp = [[NEG_INF] * (n + 1) for _ in range(n + 1)]

            for hc in range(n + 1):
                pc1_hc = pc1[hc]
                new_dp_hc = new_dp[hc]

                for hp in range(n + 1):
                    pc1_hp = pc1[hp]

                    pmx_hp = pmx[hp]
                    smx_hp = smx[hp]
                    smx0_hp = smx0[hp]

                    # Case 1: h_pp <= h_cur
                    v1 = NEG_INF
                    b1 = pmx_hp[hc]
                    if b1 != NEG_INF:
                        sc = pc1_hc - pc1_hp
                        v1 = b1 + max(0, sc)

                    # Case 2: h_pp > h_cur
                    v2 = NEG_INF
                    lo = hc + 1
                    lo2a = max(hp + 1, lo)

                    if lo2a <= n:
                        b = smx_hp[lo2a]
                        if b != NEG_INF:
                            v2 = b - pc1_hp

                    if lo <= hp:
                        b = smx0_hp[lo]
                        if b != NEG_INF:
                            v2 = max(v2, b)

                    best = max(v1, v2)
                    if best != NEG_INF:
                        new_dp_hc[hp] = best

            dp = new_dp

        # Final column handling
        ans = 0
        for hc in range(n + 1):
            for hp in range(n + 1):
                v = dp[hc][hp]
                if v == NEG_INF:
                    continue

                hi = max(hp, hc)
                sc = pre[n - 1][hi] - pre[n - 1][hc]
                ans = max(ans, v + max(0, sc))

        return ans
    