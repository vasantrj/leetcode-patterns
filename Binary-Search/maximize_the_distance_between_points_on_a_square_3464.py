"""
Problem: Maximize the Distance Between Points on a Square
LeetCode ID: 3464
Pattern: Binary Search / Greedy / Geometry
Difficulty: Hard
Time Complexity: O(n log n log P)
Space Complexity: O(n log k)

Approach:
1. Map each boundary point of the square to a 1D perimeter position.
2. Sort all perimeter positions.
3. Duplicate the array with +perimeter values to simulate circular traversal.
4. Binary search the answer d:
   - Can we choose k points such that adjacent chosen points
     on the perimeter are at least d apart?
5. For feasibility:
   - Use next-jump indices with binary lifting.
   - Greedily jump to next valid point >= current + d.
6. Return the maximum feasible distance.
"""

from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def pos(x: int, y: int) -> int:
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 2 * side + (side - x)
            return 3 * side + (side - y)

        pts = sorted(pos(x, y) for x, y in points)

        n = len(pts)
        perimeter = 4 * side
        m = 2 * n

        ext = pts + [p + perimeter for p in pts]

        LOG = max(1, (k - 1).bit_length() + 1)

        def feasible(d: int) -> bool:
            nxt = [bisect_left(ext, ext[i] + d, i + 1) for i in range(m)]
            nxt = [min(x, m) for x in nxt]

            jump = [nxt]

            for _ in range(1, LOG):
                prev = jump[-1]
                jump.append([
                    prev[min(prev[i], m - 1)] if prev[i] < m else m
                    for i in range(m)
                ])

            for i in range(n):
                cur = i
                rem = k - 1

                for j in range(LOG - 1, -1, -1):
                    if (rem >> j) & 1:
                        cur = jump[j][min(cur, m - 1)] if cur < m else m
                        rem -= 1 << j

                if cur < m and ext[cur] + d <= pts[i] + perimeter:
                    return True

            return False

        lo, hi = 0, perimeter // k

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo